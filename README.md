# WeCommunicate
A django based project where anyone can publish your stories and read other important facts and posts.
# Dependencies
  
  * python3
  * virtualenv
  * pip
  # Build and Run
  1.Clone the repository
  ```shell
  $ git clone https://github.com/muskan6769/WeCommunicate.git
  $ cd WeCommunicate
  ```
  
2. Make virtual environment on your system

```shell
$ sudo apt-get install python3-venv
$ python3 -m venv <env_name>
```
3. Activate your environment
```shell
$ source <env_name>/bin/activate
```
The virtual environment can be deactivated with the `deactivate` command.

4. Install requirements
```shell
$ pip install -r requirements.txt
```
5. Migrate files

```shell
$ python manage.py migrate
$ python manage.py makemigrations my_app
```
6. Run the app
```shell
$ python manage.py runserver
```
7. View the locally built site
```shell
localhost:8000
```
