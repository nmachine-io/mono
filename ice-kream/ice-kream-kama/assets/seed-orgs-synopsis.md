# Performing a "Big Seed"

The "Big Seed" operation runs a configurable data seeding script on the backend.

### What gets created?

The following things get created:
- n Organizations
- n Applications per organization
- n Purchases per application
- n Installs per application
- n KAMA events/errors per application

Where each n can be adjusted. 

### Is this safe in production?

You may wish to use this operation in production for demos
or employee onboarding. Otherwise, this operation should
be used for internal development. Regardless, this operation
**does not delete** existing data.

### Is this reversible?

Yes, but not through NMachine. You will have to use the 
publisher dashboard and do things there. Note that you will need
to use the "user promotion" seeding operation to implant an admin
user in each organization you wish to delete. 
