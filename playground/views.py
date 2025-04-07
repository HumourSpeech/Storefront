from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product

# Create your views here.
# REQUEST HANDLER
# request->response

def say_hello(request):
    ### MANAGERS AND QUERY_SETS(ORM concept)
        # (every model in django has an attribute called object)
        # product.objects.all :- OBJECT:-- object function is the manager object,
        #                       manager is an interface to the database
        #                       (a remote control with buttons to talk to our data base)
        #                       all:--returns the Query_Set(sql commands) to retrieve 
        #                             all the objects from product table.
        #                       get:--returns single object from the table.
        #                       filter:--for filtering data.
        #                       count:-- returns only number hence django 
        #                                does'nt return query set(not required.)
    
        # Several ways to evaluate query_set and retreive data.
    
        # query_set = Product.objects.all()

        # 1. using looping statement
        # for product in query_set:
        #     print(product)
    
        # 2. converting it into list
        # list(query_set)
    
        # 3. with indexes
        # query_set[0:5] //returns first 5 elements
    
        # product = Product.objects.all()

        # try:
        #     product = Product.objects.get(pk=0) #returns single element with primary_key = 1
        # except ObjectDoesNotExist:
        #     pass

        #better way to get object without using try catch block
        #filter returns QuerySet and first returns none if Query set is empty
        #product = Product.objects.filter(pk=0).first() 

        #to check whether the object is present not use "exists" returns boolean value
        #exists = Product.objects.filter(pk=0).exists()

    ### FILTERING DATA
        # returns all the product whose unit price is 20.
        # query_set = Product.objects.filter(unit_price=20)

        ## LOOKUP TYPES(for filtering using logical operators) CHECK OUT DOCS'Field lookups'
        # query_set = Product.objects.filter(unit_price__gt>20)
        # we also have (__lt),(__lte),(__gt),(__gte),(__range),(__startswith),(__endswith),(_istartswith),(__iendswith)
        
        # queryset = Product.objects.filter(unit_price__range=(20,30))

        # WE can also filter the relationships present in the model
        # filtering 'Collection' class which in 'Product' class as relation 'collection'
        # queryset = Product.objects.filter(collection__id__range=(1,3))

        ## LOOKUP TYPES INVOLVING STRINGS
        # queryset = Product.objects.filter(title__icontains='coffee')

        ## LOOKUP TYPES FOR DATES(can check for date, minute , month , year)
        # dates = Product.objects.filter(last_update__year=2020)

        ## LOOKUP TYPES FOR CHECKING NULL
        # queryset = Product.objects.filter(description__isnull=True)

    ### COMPLEX LOOKUPS Using Q Objects and MULTIPLE FILTERS(REFER DOCS AFTER READING NOTES)
        #One way for using multiple filters
        #queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20) 
        #Another way: using multiple filter method
        #queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

        #using Q object(can use bit wise operator which will be converted in logical operators)
        #Products: inventory < 10 OR price < 20
        #queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    
    ## USING F OBJECTS(refer Django docs)
    queryset = Product.objects.filter(inventory=F('collection__id'))

    return render(request,'hello.html',{'name':'Nitin','products':list(queryset)}) #'LAST_DATE':list(dates)})
    
