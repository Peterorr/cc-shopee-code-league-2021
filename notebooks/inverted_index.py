import pandas as pd
import csv
def main():
    df = pd.read_json("../data/raw/contacts.json")

    id_hash, label_hash = {}, {}
    for idx, row in df.iterrows():
        # Drop useless info
        row = row.drop(labels=['Id', 'Contacts'])
        # Store label list as [ Email, Phone, OrderId ]
        label_lst =  list(filter( None, row.tolist() ))
        id_hash[ idx ] = label_lst
        
        # Assign identical set object to same person in label_hash
        common_label_set = set()
        for label in label_lst:
            try:
                temp = label_hash[ label ]
                if common_label_set:
                    if common_label_set is not temp:
                        common_label_set |= temp
                        for i in common_label_set:
                            for l in id_hash[ i ]:
                                label_hash[ l ] = common_label_set
                else:
                    common_label_set = label_hash[ label ]
            
            # Create label hash if not found
            except KeyError:
                label_hash[ label ] = common_label_set
        
        # Update list object in label_hash
        common_label_set.add( idx )
        for label in label_lst:
            label_hash[ label ] = common_label_set

    # Output csv file
    with open('test.csv', "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow( ['ticket_id', 'ticket_trace/contact'] )
       
        for idx, row in df.iterrows():
            tracelst = sorted( list( label_hash[ id_hash[ idx ][0] ] ) )
            # Retrieve contact value (could be improved?)
            contactlst = [ df.iloc[x][3] for x in tracelst]
            
            tracelst = [str(x) for x in tracelst]
            csvwriter.writerow( [idx, "{}, {}".format( "-".join( tracelst), sum(contactlst) ) ]  )

if __name__ == '__main__':
    main()
