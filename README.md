# devination
A dev creativity/advice generator based on the I Ching, Oblique Strategies and Acute Strategies.
## I Ching
An ancient Chinese divination text. The meanings of the _I Ching_ symbols are many and varied.

It is, of course, complete rubish by any scientific standard - and the method of using a random number generator as opposed to the casting of lots in the physical realm makes a complete mockery of the process. As intended.

## Oblique Strategies
_Oblique Strategies_ (subtitled _Over One Hundred Worthwhile Dilemmas_) is a card-based method for promoting creativity jointly created by musician/artist Brian Eno and multimedia artist Peter Schmidt. (Source: [Wikipedia](https://en.wikipedia.org/wiki/Oblique_Strategies))

 Oblique Strategies are focused on creativity in music production, but I find that the majority are ambiguous enough that they are applicable to nearly any situation.

 ## Acute Strategies
"Acute Strategies" are compiled from several sources (and pruned to be more abstract in the spirit of Oblique):
* [Rob Blackwell](https://github.com/RobBlackwell/oblique-strategies-for-programmers)
* [traviscj](https://traviscj.com/blog/oblique_programming_strategies.html)

## How It Works
Quite simply, the system returns three random selections from each of the sources above, in respective order (I Ching, Oblique Strategy, Acute Strategy).

Example:
```
64. Wei Chi / Before Completion

Look closely at the most embarrassing details and amplify them

Are you solving the problem you have or the problem you'd like to have?
```

## How to use it
In the project directory, run the command:

```$ python app.py```

Point your browser to [http://localhost:5000](http://localhost:5000) for a poorly-formated HTML rendering of the results.

An API version is available at [http://localhost:5000/api](http://localhost:5000/api)
