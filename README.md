# Smart Elevator 
elevator offline is an offline algorithm for modern elevators demonstrated using a simulator. It takes the problem of data delivery in advance in today's elevators and solves it with a new call distribution method based on a new call system and a specific offset operation time for each elevator, which gives us better delivery and transport time.

## Getting Started
Many of us ride elevators every day. We feel like we understand how they work, how they decide where to go. If you were asked to put it into words, you might say that an elevator goes wherever it's told, and in doing so goes as far in one direction as it can before turning around. Sounds simple, right? Can you put it into code?

In this challenge, you are asked to implement the business logic for a simplified elevator model in Python. We'll ignore a lot of what goes into a real world elevator, like physics, maintenance overrides, and optimizations for traffic patterns. All you are asked to do is to decide whether the elevator should go up, go down, or stop.

### What the difference between an online algorithm and an oflline algorithm:
An online algorithm is one that can process its input piece-by-piece in a serial fashion, i.e., in the order that the input is fed to the algorithm, without having the entire input available from the beginning.
In contrast, an offline algorithm is given the whole problem data from the beginning and is required to output an answer which solves the problem at hand.

### How to run the app
```bash
# Clone the repository
$ git clone https://github.com/bsharabi/Elevator_offline_py.git
# Go into the repository
$ cd Elevator_offline_py
# Open the terminal 
$ Run "py Ex1.py <JSON Building file> <csv Call file> <output.csv>"
```

### How to run simulator
```bash
# Go to the simulator folder
$ cd Simulator
# Open the terminal
$ Run "java -jar Ex1_checker_V1.2_obf.jar <Id>,<Id> <JSON Building file> <output.csv> <out.log>"
```


### out log
after you'll run elevator online sch with simulator an output log file wile genrate at the path folder. the file show's the results of the algoritem by the parameter of time, avrage call time, unanswerd calls and avarage action time. the result are in format of:

### Result
|Call case Building | Call_a | Call_b | Call_c | Call_d|
| B1                | 112.92 | ---    | ---    | ---   |
| B2                | ---    | ---    | ---    | ---   |
| B3                | ---    | ---    | ---    | ---   |
| B4                | ---    | ---    | ---    | ---   |
| B5                | ---    | ---    | ---    | ---   |

| Call case Building |     Call_a     |     Call_b    |    Call_c    |    Call_d    |
|        :---:       |     :---:      |     :---:     |     :---:    |     :---:    |
| git status         | git status     | git status    | git status   | git status   |
| git diff           | git diff       | git diff      | git diff     | git diff     |
| git diff           | git diff       | git diff      | git diff     | git diff     |
| git diff           | git diff       | git diff      | git diff     | git diff     |








<!-- **Note**: Running this requires [Git](https://git-scm.com) and [npm](https://www.npmjs.com/).
https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/ -->