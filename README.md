# 🗓️ <u>Python Multi-Thread Tutorial</u> 

This repo is about demonstrating **concurrency/parallelism** knowledge using python. 

---

### 📍 Beginner to Intermediate

We'll walkthough the foundations of mutlti-threaded programs using python.

1. [Day 1 - Introduction to Threads](https://github.com/abhilashmendhe/python-multi-thread-programs/tree/main/day1)

    In **day one**, we covered basics of threads and process. Written a basic python code about how the threads are being called and executed.

2. [Day 2 & 3 - Creating and starting threads, and passing arguments to threads](https://github.com/abhilashmendhe/python-multi-thread-programs/tree/main/day2)

    In **day two**, we used python libraries like <span style="background-color: #b8b8b8f1;">threading.Thread</span>, <span style="background-color: #b8b8b8f1;">start()</span>, <span style="background-color: #b8b8b8f1;">join()</span>, and created 5 individual threads by printing its name.
    In **day three**, we passed arguments to threads.

4. [Day 4 - Daemon Threads](https://github.com/abhilashmendhe/python-multi-thread-programs/tree/main/day4)

    In **day 4**, we coverd the topic of _foreground_ vs _background_ threads, _daemon_ threads. Created a basic program where _daemon_ thread is running infinitely and exits when the main stops.

5. [Day 5 - Thread Synchronization (Locks)](https://github.com/abhilashmendhe/python-multi-thread-programs/tree/main/day5)

    In **day 5**, we studied the concepts of __race conditions__, and **locks**. Simulated a basic bank app where money is deposited and withdrawed using locks making it concurrent safe.

6. [Day 6 - Thread Communication (Queue)](https://github.com/abhilashmendhe/python-multi-thread-programs/tree/main/day6)

    In **day 6**, we studied the concepts of <span style="background-color: #b8b8b8f1;">queue.Queue</span> where no _locks_ are required, and covered producer/consumer topic. 
    Simulated the same banking application only using queues(channels).

7. [Day 7 - Mini project 1](https://github.com/abhilashmendhe/python-multi-thread-programs/tree/main/day7-mini-project)

    In **day 7**, created a mini-project that simulates the actual restaurant operations. 

8. [Day 8 - Mini project 2](https://github.com/abhilashmendhe/python-multi-thread-programs/tree/main/day8-mini-project)

    In **day 8**, created a file downloader with multiple threads using producer-consumer.