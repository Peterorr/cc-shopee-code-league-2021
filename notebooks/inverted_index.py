import pandas as pd
import csv
def main():
    df = pd.read_json("../data/raw/contacts.json")
    id_hash, label_hash = {}, {}

    for idx, row in df.iterrows():
        
        # Get contact value before dropping it
        contact = row[3]

        # Drop useless info
        row = row.drop(labels=['Id', 'Contacts'])
       
        # Store label list as [ Email, Phone, OrderId ]
        label_lst =  list(filter( None, row.tolist() ))
        id_hash[ idx ] = label_lst
        
        # Assign same list object to same person in label_hash
        common_contact_lst, common_label_lst = [], []
        for label in label_lst:
            try:
                common_contact_lst, common_label_lst = label_hash[ label ]
            except:
                # Recreate label hash if not found
                label_hash[ label ] = common_contact_lst, common_label_lst
        
        # Update list object in label_hash
        common_label_lst.append( idx )
        common_contact_lst.append( contact )
        for label in label_lst:
            label_hash[ label ] = common_contact_lst, common_label_lst

    # Output csv file
    with open('test.csv', "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow( ['ticket_id', 'ticket_trace/contact'] )
        
        for idx, row in df.iterrows():
            contactlst, tracelst = label_hash[ id_hash[ idx ][0] ]
            tracelst = [str(x) for x in tracelst]
            csvwriter.writerow( [idx, "{}, {}".format( "-".join( tracelst), sum(contactlst) ) ]  )
    
   
    
    




if __name__ == '__main__':
    main()
