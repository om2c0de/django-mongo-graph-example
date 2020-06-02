"""
GraphQL queries list:


# How it looks on MongoDB level
> db.barrel_rates.find()
> show collections
barrel_rate
> db.barrel_rate.find()
{ "_id" : ObjectId("5ed65c136aaecb610d34bb31"), "value" : 120 }
{ "_id" : ObjectId("5ed65e16ac7cca5353e81f1e"), "value" : 120 }
{ "_id" : ObjectId("5ed65e91fe7d6256b0f6f66c"), "value" : 120 }
{ "_id" : ObjectId("5ed6615425523ddb52d26ba1"), "value" : 122 }
>


# Get first object

{
   barrelRates(first: 1){
       edges {
           node {
               id,
               value
           }
       }
   }
}

# Create new one

mutation {
    barrelRateCreate(barrelRateData:{value: 120})
    {
        barrelRate{
            value
        }
    }
}

# Update one

mutation {
    barrelRateUpdate(barrelRateData:{
        id: "5ed65c136aaecb610d34bb31",
        value: 777
    }) {
        barrelRate {
            value
        }
    }
}


# Remove one

mutation {
    barrelRateDelete(objectId: "5ed65c136aaecb610d34bb31") {
        success
    }
}

"""