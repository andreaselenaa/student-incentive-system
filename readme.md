# Staff logs hours for a student
```bash
$ python wsgi.py staff log-hours 101 12

```

Output:
```bash
Staff logged 12 hours for Student #101
```


# Student requests confirmation of hours
```bash
$ python wsgi.py student request-confirmation 101


```

Output:
```bash
Request sent to staff for confirmation of Student #101's hours

```


# Staff confirms the student’s hours
```bash
$ python wsgi.py staff confirm-request 101


```

Output:
```bash
Staff confirmed hours for Student #101

```


# Student views accolades
```bash
$ python wsgi.py student view-accolades 101


```

Output:
```bash
Student #101 has earned the 10 Hours Milestone!

```



# Student views leaderboard
```bash
$ python wsgi.py student view-leaderboard


```

Output:
```bash Student Leaderboard
1. Student #101 — 12 hours
2. Student #102 — 8 hours
3. Student #103 — 5 hours

```
