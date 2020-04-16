# catchall-inbox-server
API to fetch emails from a catchall inbox for easy testing

When running locally, best to use a virtual environment.
Then run:

```
pip install -r requirments.txt
```

To set your credentials for your mail server, set the following variables:

```
CATCHALL_HOSTNAME
CATCHALL_USERNAME
CATCHALL_PASSWORD
```

Alternatively, copy the credentials-example.yml to credentials.yml and set the credentials there.

After setting the credentials, run the application with:

```
waitress-serve catchallinbox:app
```
