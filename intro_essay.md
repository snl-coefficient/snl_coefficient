Mean Girls is a *Saturday Night Live* film, and other data findings 
==================================================================

By Emily Esten and Kathrine Esten

Introduction 
For mathematics scholars, there is the “Erdös number”; for film and other media buffs, the “Bacon number” is a facsimile. [^1] Both explore degrees of connection: how do professionals in a field interact and find connections with one another? Our project takes the long-running variety sketch comedy show *Saturday Night Live* and considers its potential impact on media production (ie. films, television, podcasts, etc.) 

While not an individual, *Saturday Night Live* has functioned as a consistent entity in American entertainment as the longest-running sketch comedy show on American television, as well as the longest-running variety show in U.S. history. [^2] Much has written about *SNL* stars' success and fame, as well as the show's impact in the political realm, but less so on the cast's influence within the comedy industry. In order to focus on the potential impact of the show on media production, we have developed the *SNL* Coefficient, inspired by the concept of the Erdös/Bacon numbers, but finding connections between pieces of media (ie. a film and *SNL*) rather than two professionals in the field. 

## Why *SNL*?
Now in its 48th season, SNL is known its massive collection of alumni. Projects produced by current and former cast are often related back to their role on the show: 

Tina Fey (Former *SNL* head writer and repertory player, 1997-2006) began her foray into film while still behind the Weekend Update desk in Studio 8H. The filming of *Mean Girls* (2004) coincided with the 29th *SNL* season. [^3] It isn’t surprising, then, that *SNL* is cited so frequently in the film’s reviews, whether as praise for Fey herself (“...a live wire: a sexy “Weekend Update” funny girl who rarely sends out a joke without a sting in its tail… brings her sass as an actress and a writer…”) or in reference to the presence of Lorne Michaels as producer.[^4] 

It is standard, to refer to the work that a writer/actor/director/producer is best known for at the time of a project’s release. *Anchorman* (2004) came two years after star Will Ferrell’s departure from *SNL* but still drew comparison: Empire claimed the film had the “hit-and-miss quality of an extended *Saturday Night Live sketch*.”[^5] 

Yet, 15 years after Adam Sandler and Fred Wolf left *SNL*, mentions of the show continued to spring up in reviews of *Grown Ups* (2010), suggesting that for many alum, *SNL* retains a key aspect of their professional resume. 

## What is an *SNL* film?
Returning to our earlier point – focusing on *SNL* and other media entities rather than individuals – we consider the so-called “*SNL* film.” In various fan-centric rankings, there are between 11 and 14 “*SNL* films” as of 2022. [^7][^8][^9].
Standards for inclusion appear to be:
1. Derived from a sketch first appearing on *SNL* (see: *Wayne’s World* (1992))
2. Released outside of the confines of Studio 8H (see: *Gilda Live* (1980))
3. Involving *SNL* cast members, past and/or present (see: *Coneheads* (1993))

Other standards are difficult to tie down without eliminating (or including) certain projects. Does it need the involvement of Lorne Michaels or other *SNL* producers? Eliminate *Blues Brothers* (1980). Must all original cast members appear? Eliminate *Blues Brothers 2000* (2000). Does it need to be a feature length film? If not, *The David S. Pumpkins Halloween Special* (2017) belongs somewhere in the lineup.

These standards, however, films that arguably wouldn’t exist as we know them without *Saturday Night Live*: the aforementioned *Mean Girls*, *Anchorman*, and *Grown Ups* to name a few. To best represent this analysis – a film or television show or media project’s relationship to *Saturday Night Live*’s sphere of influence, we developed the *SNL* Coefficient.

## The *SNL* Coefficient 
Using sources from IMBD, Wikipedia, and dedicated *SNL* fans, we identified credited *SNL* cast members and writers (collectively *SNL* alums). After confirming their role on the show, we collected additional data regarding active years on the show and their role as writer, actor or both. Special consideration was given to “Weekend Update” hosts – a guaranteed weekly presence on the show – as well as alums who have returned to host. 

Once this dataset was compiled, we found the IMBD pages for each *SNL* alum and scraped their entire filmography. We reviewed these credits to filter for media properties that were released during and after their time on *SNL* and for which the alum was credited as writer, director, producer, actor/actress, self, or present in archival footage. Any media property that involved two or more *SNL* alums was deemed "*SNL*-related media".

Using the additional information that we'd collected from IMDB regarding their time with *SNL*, we calculated a coefficient for each *SNL* alum using the following formula:
- 10% Number of Episodes Hosted (number of episodes hosted/number of most hosted times)
- 10% Best Of compilations (a 0/1 value)
- 15% Number of Episodes with Weekend Update
- 15% Number of Seasons as Head Writer
- 25% Number of Episodes (46% Credited on Show as Actor, 44% Credited on Show as Writer, 10% for Other Credits)
- 25% Number of Seasons (46% Credited on Show as Actor, 44% Credited on Show as Writer, 10% for Other Credits)

Acting credits are weighted slightly more heavily in the formula, given that actors also serve as uncredited writers throughout the season and are more visibly associated with the show from a general audience perspective.) We recognize there are limitations with this system - Lorne Michaels, for example, would have a middling coefficient had we not given him a base coefficient of 1. This formula also relies heavily on quantity of *SNL* associations, as opposed to quality, and heavily favors more recent alums who have stayed on the show for longer periods of times than alums who were on the show in its early years.

For example (as of publication):
- Tina Fey hosted *SNL* 6 times between 2008 and 2018.
- Fey does not have a Best Of compilation, so she is given a value of 0.
- Fey has hosted “Weekend Update” on 117 episodes.
- Fey has served 7 seasons as head writer.
- Fey has been involved in XX episodes, including XX as actor, XX as writer, and XX for other.
- Fey served 9 seasons on the show from 1997 to 2006: 6 as an actor (5 as repertory player and 1 as featured player) and 9 as writer (7 as head writer).
- Fey has a coefficient of XX.

For any *SNL*-related media, we scraped additional information from IMDB about the media's genres, number of episodes, principal cast and crew, and production companies. We then calculated a movie coefficient for each "*SNL*-related media" property using the following formula:
- For each *SNL* alum credit in the *SNL*-related media, we weighted their coefficient based on involvement in the property (percentage of episodes). For movies or other non-episodic media, the percentage of episodes is 1. If the alum served a particularly important role in the property (one of the principal cast/crew or a producer), their value was multiplied by a role coefficient of 2.
- The sum of these *SNL* alum values was increased by a value of 5 if the *SNL*-related media was directly associated with *SNL* (a "Best Of" compilation, a spin off, a movie based on an *SNL* sketch, etc.)
- The sum was then divided by the number of *SNL* credits associated with the show, before being multiplied by the number of alums who participated.  

For example:
*Mean Girls* involved 5 *SNL* alumni: Ana Gasteyer, Lorne Michaels, Amy Poehler, Tim Meadows, and Tina Fey. Fey is credited twice (as writer and performer) and so her coefficient will be considered twice.
```
< AG + LM + AP + TM + TF + TF >
```
Since this is a movie, their coefficients are each multiplied by 1.
```
< AG + LM + AP + TM + TF + TF >
```
Only Tina Fey (screenplay and star) is considered a principal person according to IMDB (though Tim Meadows, Amy Poehler, and Ana Gasteyer have top-billing and Lorne is a producer). Her coefficient is multiplied by 2 for each credit.
```
< AG + LM + AP + TM + (TF*2) +( TF*2) >
```
Mean Girls was not directly associated with *SNL*, so there is no increased value.
```
< AG + LM + AP + TM + (TF*2) +( TF*2)  + 0 >
```
At the time of writing, the sum of the coefficients equaled XX. Divided by 6 (the number of *SNL* alumni credits), and then multiplied by 5 (the number of *SNL* alumni), the coefficient then equals XX.
```
((AG + LM + AP + TM + (TF*2) +( TF*2) )/6)/5 = coefficient
```

## Findings of Interest 

As one might expect, official *SNL* media makes up the majority of the high-coefficient items in the dataset. However, our results also showed: 
- Only 29 TV series meet the qualifications of *SNL* Movie, 4 of which are already “*SNL*-related media”. All of these fall into the Comedy genre - think *Portlandia*, *30 Rock*, *Shrill*, and *Schmigadoon*!
- Only 1 podcast fits the bill: *Heads Will Roll* (2020), a raunchy audio comedy co-created by Kate McKinnon.
- 8 of Happy Madison Productions meet *SNL* film criteria, and most of them come after the release of *Grown Ups* (2010).
- Some high profile ensemble films with *SNL* alum didn’t make the cut, including *Bridesmaids* (2011). 
- Adam Sandler and Will Ferrell both fall in the top 20% of *SNL* alumni based on coefficients.
- Excluding Michaels, the average coefficient for an *SNL* alum is XX (writers vs. actors?). The cohort with the highest average coefficient is XX, which features alums such as …

## What's Next?

*Saturday Night Live* is self-aware of its longstanding impact on its alumni and the broader entertainment industry with the presence of the “Five-Timers Club” sketches for oft-returning hosts and highly anticipated episodes with returning cast members as hosts or guest stars, as seen with Maya Rudolph’s portrayal of Kamala Harris. [^10]
 
For industry professionals, the data may provide hope that networking with an individual with a higher *SNL* coefficient might provide access to a wealth of connections – the authors of this article provide no guarantees about this path.

For academics and fans of the show, the data provides a starting point about the post-*SNL* prospects and opportunities available to alums of the show and aspiring comics. *SNL*, while oft researched for its influence on political events or its challenges to gender representation, started as a challenge to the comedy industry. But looking at the networks and media-making opportunities created as offshoots of *Saturday Night Live*, we can see that certain generations of actors have fueled some of the most successful comedy films and television series of the past decades using their *SNL* connections.

Nick Marx, an associate professor of film and media studies at Colorado State University, proposed that *SNL* is today a “nexus between two talent pools”: up-and-coming comedians trying to attract attention and established comedians satiating an audience demand for content. [^11]. With more forms of popular media available to performers today than ever before, from webseries to Hollywood films to television shows on a dozen different streaming services, expanding the *SNL* media universe is a critical step forwards in media analysis.

Works Cited
[^1]: The Erdös Number Project. (2020, June 6). “Items of Interest Related to Erdös number.” Oakland University. https://www.oakland.edu/enp/related/
[^2]: Nunan, Tom. (2021, January 29). “Saturday Night Live, America’s Longest Running Sketch Variety Show, Posts #1 Comedy Ranking” Forbes.com. https://www.forbes.com/sites/tomnunan/2021/01/29/saturday-night-live-americas-longest-running-sketch-variety-show-posts-1-comedy-ranking/?sh=127b1c086406 
[^3]: Shofner, Melissa Raé and Lauri S. Friedman. (2016, December 15). Tina Fey: The Queen of Comedy. Greenhaven Publishing LLC. https://books.google.com/books?id=qH1mDwAAQBAJ&pg=PA44&lpg=PA44&dq=mean+girls+reviews+%22snl%22&source=bl&ots=fg-svdpzsa&sig=ACfU3U3H5LnfO9vrTnpDbvWIaYylcZvkzA&hl=en&sa=X&ved=2ahUKEwjO9OONi6T2AhWCct8KHQWQDcU4FBDoAXoECCUQAw#v=onepage&q=mean%20girls%20reviews%20%22snl%22&f=false 
[^4]: Ebert, Rogers. (2004, April 30). “Mean Girls.” RogerEbert.com. https://www.rogerebert.com/reviews/mean-girls-2004
[^5]: Thomas, William. (2004). “Anchorman: The Legend of Ron Burgundy Review.” Empire. https://www.empireonline.com/movies/reviews/anchorman-legend-ron-burgundy-review/ 
[^6]: Sharkey, Betsey. (2010, June 25). “Movie review: ‘Grown Ups’.” Los Angeles Times. https://www.latimes.com/archives/la-xpm-2010-jun-25-la-et-grown-ups-20100625-story.html 
[^7]: Boone, Brian. (2018, October 12). “Every Saturday Night Live Movie, Ranked.” Vulture. https://www.vulture.com/2018/10/best-snl-movies-ranked.html 
[^8]: Singer, Matt. (2020, September 9). “Every ‘Saturday Night Live’ Movie Ranked from Worst to Best.” Screen Crush. https://screencrush.com/every-saturday-night-live-movie-ranked/
[^9]: West, Rachel. (2020, May 21). “Highest Grossing ‘SNL’ Movies.” ET Canada. https://etcanada.com/photos/646647/highest-grossing-snl-movies/#image-646684
[^10]: Saturday Night Live. (2022, February 27). “Five-Timers Club.” YouTube. https://www.youtube.com/watch?v=W-gy_b5cPlo 
[^11]: Marx, Nick and Matt Sienkiewicz and Ron Becker. (2013). Saturday Night Live and American TV. Bloomington: Indiana University Press. 