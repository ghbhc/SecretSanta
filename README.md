# SecretSanta
Randomly generate Secret Santa matches.  The script will ensure that you do not get yourself or your romantic partner.

## Requirements

Python >= 3.6

## How to use

Prepare your input file with one participant listed per line, unless they have a romantic partner also playing, in which case put both people on the same line, separated by a comma, as shown in sample_input.txt.

```
./ss.py input.txt
```

This will create an "assignments" directory (in your current dir, if it doesn't already exist) in which there will be a text file named after each participant, whose content will be the person's name who they're assigned to give a gift to.  It creates individual text files like this so that the person running the script doesn't have to spoil who got who for themselves.  You can individually email the txt files to each participant.

### Example Run

```
ben@ubuntu:~/Git/SecretSanta$ ./ss.py sample_input.txt

Assigning partners...

beep bop boop...

ben@ubuntu:~/Git/SecretSanta$ ls assignments/
Aaron.txt  Alexis.txt  Ben.txt  Kaley.txt  Luis.txt  Maralyn.txt  Missy.txt  Nic.txt
ben@ubuntu:~/Git/SecretSanta$ awk '{print $0}' assignments/Ben.txt
Nic
ben@ubuntu:~/Git/SecretSanta$ 
```
