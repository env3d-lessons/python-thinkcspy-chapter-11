# IMDb File Lab

This lab is all about working with files.  The gerenal pattern for working
with files to use loops and process a file one line at a time.

The typical reason why we work with files is because these files are too big or
change all the time so the data cannot be included inside our program.  

For this lab We are going to use data from IMDb (Internet Movie Database).  I
have prepared 2 data files for you (only contains data from 2020-present):

 - title.basics.tsv.gz - Contains the following fields for titles:

    tconst (string) - alphanumeric unique identifier of the title
    titleType (string) – the type/format of the title (This file only contain movie type)
    primaryTitle (string) – the more popular title / the title used by the filmmakers 
                            on promotional materials at the point of release
    originalTitle (string) - original title, in the original language
    isAdult (boolean) - 0: non-adult title; 1: adult title
    startYear (YYYY) – represents the release year of a title.
    endYear (YYYY) – TV Series end year. \\N for all other title types
    runtimeMinutes – primary runtime of the title, in minutes
    genres (string array) – includes up to three genres associated with the title
    
 - title.ratings.tsv.gz – Contains the IMDb rating and votes information for titles
 
    tconst (string) - alphanumeric unique identifier of the title
    averageRating – weighted average of all the individual user ratings
    numVotes - number of votes the title has received

These files are similar to chapter 11.4 of the textbook in that you 
can use line.split() to separate each line into fields.

The details of these files can be found at https://www.imdb.com/interfaces/

## Notes

- Movie titles are **case sensitive** and use underscores (`_`) instead of spaces.
- Read the comments for each function and implement what is required.

# Submission

Run `pytest` to check your code.  When satisfied, submit your code with the following command 
in the terminal:

```bash
git add -A
git commit -m "submit"
git push
```
