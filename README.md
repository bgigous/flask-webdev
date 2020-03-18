To get started with development with python 3.7 or higher:

```bash
python3 -m venv env
. env/bin/activate
pip install -r requirements/dev.txt
source development.sh
```

Then start a `flask shell` session and enter the following:

```bash
flask shell
```
```python
>>> db.create_all()
>>> Role.insert_roles()
>>> exit()
```

If you want the app to send emails, including confirmation emails, you must have an email that accepts SMTP authentication. Should you have such an email set up correctly, you must then set the environment variables `MAIL_USERNAME`, `MAIL_PASSWORD`, and `RAGTIME_ADMIN`. Below is an example bash script you can `source` to enable email-sending capabilities:

```bash
# MAIL_PASSWORD depends on your email provider
export MAIL_USERNAME=yourusername
export MAIL_PASSWORD=<password or app password>
export RAGTIME_ADMIN=yourusername@example.com
```

If you want to bypass the confirmation email in order to access the site, enter another `flask shell` session and type:

```bash
flask shell
```
```python
u = User.query.filter_by(username='<your username>').first()
u.confirmed = True
db.session.commit()
quit()
```

Have fun. c: