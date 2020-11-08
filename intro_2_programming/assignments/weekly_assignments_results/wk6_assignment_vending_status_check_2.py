import json 

class inv_item:
    def __init__( self, item_nam ):
# name of the bev only one per inv_item

        self.name = item_nam
# tot num  of this beverage stock per mach
        self.tot_stock = 0
# tot numb of this bev still in mach
        self.tot_n_stock = 0
# The tot numb of bev slots
        self.tot_slots = 0
  
    def add_2_stock( self, stockAmt ):
        self.tot_stock = self.tot_stock + stockAmt
  
    def add_2_n_stock( self, inStockAmt ):
        self.tot_n_stock = self.tot_n_stock + inStockAmt
  
    def incr_slots( self ):
        self.tot_slots = self.tot_slots + 1

    def gt_num_sld( self ):
        return self.tot_stock - self.tot_n_stock
  
    def gt_pct_sld( self ):
        return self.gt_num_sld() / self.tot_stock
  
# based on 8

    def gt_stock_nded( self ):
        return 8 * self.tot_slots - self.tot_n_stock
  
    def gt_nam( self ):
        return self.name

    def gt_num_n_stock( self ):
        return self.tot_n_stock

    def __repr__( self ):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format( self.name, self.tot_n_stock, self.tot_stock, self.tot_slots )
  
class mach_stat:
    def __init__(self, mach_nam):
        self.name = mach_nam
        self.prior_bev_stock = 0
        self.curr_bev_stock = 0
        self.tot_inc = 0.0
  
    def gt_sld_pct(self):
        return (self.prior_bev_stock - self.curr_bev_stock) / self.prior_bev_stock * 100
  
    def updat_inc(self, income):
        self.tot_inc = self.tot_inc + income
    
    def updat_prior_bev_stock(self, prevBevStock):
        self.prior_bev_stock = self.prior_bev_stock + prevBevStock
    
    def updat_curr_bev_stock(self, curr_bev_stock):
        self.curr_bev_stock = self.curr_bev_stock + curr_bev_stock
    
    def gt_nam(self):
        return self.name
    
    def gt_curr_stock(self):
        return self.curr_bev_stock
    
    def gt_prior_stock(self):
        return self.prior_bev_stock
    
    def gt_tot_inc(self):
        return self.tot_inc
    
    def __repr__(self):
        return "Name {}, Income {}, Sold Pct {:2f}".format(self.name, self.tot_inc, self.gt_sld_pct())
  
  
def main():
    inv_file_nam = ["REID_1F_20171004.json", "REID_2F_20171004.json", "REID_3F_20171004.json"]
    
    # dic that maps name of bevs 
    item_nam_2_inv_item = {}
    mach_stat_dict = {}
    
    # inv file
    for inv_fil_nm in inv_file_nam:
        inv_file = open( inv_fil_nm, 'r' )
        
        
        # read json dict
        inv_dat = json.loads( inv_file.read() )

        mach_nam = inv_dat['machine_label']

        mach_status = mach_stat_dict.get( mach_nam, mach_stat(mach_nam) )
        
        contents = inv_dat['contents']
        
        # rows in vend mach
        for row in contents:
  
# bev slots
            for slot in row['slots']:
                item_nam = slot['item_name']
            # Get the inv_item for this beverage using its name as the key 
            inv_items = item_nam_2_inv_item.get( item_nam, inv_item( item_nam ) )
            
            # Update  this inv_item, adding in how many beverages were stocked 
            inv_items.add_2_stock( slot['last_stock'] )
            inv_items.add_2_n_stock( slot['current_stock'] )
            inv_items.incr_slots();
            
            mach_status.updat_inc(slot['item_price']*(slot['last_stock']-slot['current_stock']))
        mach_status.updat_prior_bev_stock(slot['last_stock'])
        mach_status.updat_curr_bev_stock(slot['current_stock'])
  
# Store this inv_item object in the dict
        item_nam_2_inv_item[item_nam] = inv_items

    mach_stat_dict[mach_nam] = mach_status
        # report options
    srt_by_choice = input('Would you like the (m)achine report or (i)nventory report? ')
        # list of inv items
    inv_item_ls = list( item_nam_2_inv_item.values() )
    mach_stat_ls = list(mach_stat_dict.values())

    if srt_by_choice == 'm':
        print('{:15} {:15} {:10}'.format('Machine Name', 'Percent Sold', 'Sales Total'))
        for item in mach_stat_ls:
            print('{:10} {:10.2f}% ${:8.2f}'.format(item.gt_nam(), item.gt_sld_pct(), item.gt_tot_inc()))
    elif srt_by_choice == 'i':
        while srt_by_choice != 'q':
            srt_by_choice = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
  
# usr options for pulling data
            if srt_by_choice == 'n':
                inv_item_ls.sort( key=inv_item.gt_nam )
            elif srt_by_choice == 'p':
                inv_item_ls.sort( key=inv_item.gt_pct_sld )
                inv_item_ls.reverse()
            elif srt_by_choice == 's':
                inv_item_ls.sort( key=inv_item.gt_stock_nded )
                inv_item_ls.reverse()
  
# Output 
            print( 'Item Name Sold % Sold In Stock Stock needs')
            for item in inv_item_ls:
                print( '{:20} {:8} {:8.2f}% {:8} {:8}'.format( item.gt_nam(), item.gt_num_sld(), item.gt_pct_sld() * 100, item.gt_num_n_stock(), item.gt_stock_nded()))
            print()
  
main()