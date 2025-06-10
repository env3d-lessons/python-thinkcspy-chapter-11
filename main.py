"""
Exercise 1

Unlike a list, you cannot simply use the len() function find 
out how many lines a file has.  You have to actually loop over 
a file an use the accumulator pattern to count the lines.

Using the technique described in 
https://runestone.academy/ns/books/published/thinkcspy/Files/Iteratingoverlinesinafile.html
complete the following function so it returns the number of 
lines in the file title.basics.tsv
"""


def count_titles():
    f = open('title.basics.tsv')
    count = 0
    for line in f:
        count += 1
    f.close()
    return count


"""
Exercise 2

In the file title.basics.tsv, the 5th field contains a string indicating
if the title belongs in the "adult" category.  Complete the following 
function which returns the number of adult titles in title.basics.tsv.

You will need to first split each line into fields (as shown in 11.4), 
and then use an IF statement inside the loop to selectively count the titles.

"""
def count_adult_titles():
    f = open('title.basics.tsv')
    count = 0
    for line in f:
        fields = line.strip().split()
        if len(fields) > 4 and fields[4] == '1':
            count += 1
    f.close()
    return count

"""
Exercise 3

Similar to the previous exercise, but count the number of "Romance" titles.

Note that the genre is stored in the 9th field, but since a movie can have mutiple
genres, it is a string separated by commas.

For example, the following is the entry for 'The Hunger Games':
tt1392170 movie The_Hunger_Games The_Hunger_Games 0 2012 \\N 142 Action,Adventure,Sci-Fi

It belongs to 3 genres: Action, Adventure, and Sci-Fi

"""
def count_romance_titles():
    f = open('title.basics.tsv')
    count = 0
    for line in f:
        fields = line.strip().split()
        if len(fields) > 8 and 'Romance' in fields[8].split(','):
            count += 1
    f.close()
    return count

"""
Exercise 4

Give a movie_title as input, output its title id (field #1)
If the title is not found, return the empty string ''.

Note that titles are case sentitive and words are separated by underscore (_)

> find_title_id('The_Hunger_Games')
'tt1392170'
> find_title_id('The_Avengers')
'tt0848228'
> find_title_id('avengers')
''

"""
def find_title_id(movie_title):
    f = open('title.basics.tsv')
    for line in f:
        fields = line.strip().split()
        if len(fields) > 2 and fields[2] == movie_title:
            f.close()
            return fields[0]
    f.close()
    return ''

    
"""
Exercise 5

Give a movie_title as input, output its IMDB rating
If the title is not found, return -1.

Note that titles are case sentitive and words are separated by underscore (_)

> get_rating('The_Hunger_Games')
7.2
> get_rating('The_Avengers')
8.0
> get_rating('avengers')
-1.0 


"""
def get_rating(movie_title):
    # First, find the title id from title.basics.tsv
    title_id = ''
    f = open('title.basics.tsv')
    for line in f:
        fields = line.strip().split()
        if len(fields) > 2 and fields[2] == movie_title:
            title_id = fields[0]
            break
    f.close()
    if title_id == '':
        return -1.0

    # Now, look up the rating in title.ratings.tsv
    f = open('title.ratings.tsv')
    for line in f:
        fields = line.strip().split()
        if len(fields) > 1 and fields[0] == title_id:
            try:
                rating = float(fields[1])
                f.close()
                return rating
            except:
                f.close()
                return -1.0
    f.close()
    return -1.0


### DO NOT MODIFY ANYTHING BELOW THIS LINE ###
### The following code is for the Gradio UI, which allows users to interact with the functions defined above.

if __name__ == "__main__":
    import gradio as gr

    def ui_count_titles():
        return count_titles()

    def ui_count_adult_titles():
        return count_adult_titles()

    def ui_count_romance_titles():
        return count_romance_titles()

    def ui_find_title_id(movie_title):
        return find_title_id(movie_title)

    def ui_get_rating(movie_title):
        return get_rating(movie_title)

    with gr.Blocks() as demo:
        gr.Markdown("# IMDb File Lab UI")

        with gr.Tab("Count Titles"):
            count_btn = gr.Button("Count All Titles")
            count_out = gr.Number(label="Total Titles")
            count_btn.click(fn=ui_count_titles, outputs=count_out)

        with gr.Tab("Count Adult Titles"):
            adult_btn = gr.Button("Count Adult Titles")
            adult_out = gr.Number(label="Adult Titles")
            adult_btn.click(fn=ui_count_adult_titles, outputs=adult_out)

        with gr.Tab("Count Romance Titles"):
            romance_btn = gr.Button("Count Romance Titles")
            romance_out = gr.Number(label="Romance Titles")
            romance_btn.click(fn=ui_count_romance_titles, outputs=romance_out)

        with gr.Tab("Find Title ID"):
            title_input = gr.Textbox(label="Movie Title (case sensitive, underscores)")
            id_btn = gr.Button("Find Title ID")
            id_out = gr.Textbox(label="Title ID")
            id_btn.click(fn=ui_find_title_id, inputs=title_input, outputs=id_out)

        with gr.Tab("Get Rating"):
            rating_input = gr.Textbox(label="Movie Title (case sensitive, underscores)")
            rating_btn = gr.Button("Get Rating")
            rating_out = gr.Number(label="IMDb Rating")
            rating_btn.click(fn=ui_get_rating, inputs=rating_input, outputs=rating_out)


    demo.launch()

