# Seeding an Admin

This operation invokes the `seed:admin` rake task from
[`/lib/tasks/seeding_tasks.rake`](https://github.com/nmachine-io/mono/blob/master/ice-kream/ice-kream-app/lib/tasks/seeding_tasks.rake),
which creates an `AdminUser` in the application database, with which
you can then authenticate at `/admin/auth`. 

<br/>

The email and password must be valid, e.g correct format and strength 
(8 characters, 1 or more symbol, 1 or more number, lower and upper cases).
The request will be ignored if an admin user with the same email address
already exists.


## Can I Create More Admins?

You should only use this operation if you do **not** have access
to the admin panel. If you do have access to the admin panel, 
navigate to `/admin/admin_users` and choose "Create New".

## What if I Forget the Password?

If you loose access to an admin you created using this operation,
you should:
1. Run this operation again with **new email**
1. Log into the admin panel and **delete the old account** 
