<p align = "center">
  <a href="http://datascience.disco.unimib.it/it/"><img src ="https://raw.githubusercontent.com/malborroni/Foundations_of_Computer-Science/master/images/DSunimib.png" width = "100%"></a>
</p>
<p align="center">
  <img src="https://github.com/malborroni/Just-Repeat-Hit/blob/master/Images/logo_with_title.png" width="55%">
</p>
  <h6 align="center">a Data Management and Data Visualization Project</h6>
<p align="center">
  <a href="#overview">Overview &nbsp;</a> |
  <a href="#visualizations">&nbsp; Visualizations &nbsp;</a> |
  <a href="#references">&nbsp; References &nbsp;</a> |
  <a href="#data">&nbsp; Data &nbsp;</a> |
  <a href="#presentation">&nbsp; Presentation &nbsp;</a> |
  <a href="#aboutus">&nbsp; About us &nbsp;</a>
</p>

<a name="overview"></a>
## &#9741; &nbsp; Overview
The musical world of recent years seems to be characterized by increasingly repetitive, obvious and banal hits.
This project, therefore, aims to measure the repetitiveness of the songs, analyzing them from a textual point of view, with the aim of assessing the existence or otherwise of certain trends.<br>
The approach used exploits the calculation of an indicator, called the "Repetitiveness Index", which corresponds to the complement of the relationship between the unique words within a text, ie those words that are present once and only once, and the total words of the same.<br>
Greater attention was paid to the study of the time course of the average Repetitiveness Index and to the analysis of the same index, focusing mainly on an aggregation based on the musical genre.

Main goals:
- to identify of the obvious directions in the trend of the index;
- to identify which musical genres were more or less repetitive, also trying to understand how the lyrics of the songs could influence these results.

<a name="visualizations"></a>
## &#9741; &nbsp; Visualizations
Through the use of the Tableau software, some infographics have been proposed that allow you to obtain a more detailed insight on the results, with the aim of understanding them better.

<br>
<p align="center">
  <a href="https://public.tableau.com/shared/XN9MSMJNN?:toolbar=n&:display_count=y&:origin=viz_share_link"><img src = "https://github.com/malborroni/Just-Repeat-Hit/blob/master/Visualizations/3_analisi_indice_tempo.PNG" width = "80%"></a>
</p>

<p align="center">
  <a href="https://public.tableau.com/shared/TXRH7KBJT?:toolbar=n&:display_count=y&:origin=viz_share_link"><img src = "https://github.com/malborroni/Just-Repeat-Hit/blob/master/Visualizations/4_distribuzione_ripetitivit%C3%A0.PNG" width = "80%"></a>
</p>

<p align="center">
  <a href="https://public.tableau.com/shared/RGNBKKFRF?:toolbar=n&:display_count=y&:origin=viz_share_link"><img src = "https://github.com/malborroni/Just-Repeat-Hit/blob/master/Visualizations/5_ripetitivit%C3%A0_x_genere.PNG" width = "80%"></a>
</p>

<p align="center">
  <a href="https://public.tableau.com/shared/FJF32GMJ2?:toolbar=n&:display_count=y&:origin=viz_share_link"><img src = "https://github.com/malborroni/Just-Repeat-Hit/blob/master/Visualizations/6_ripetitivit%C3%A0_per_canzoneartista.PNG" width = "80%"></a>
</p>


To access the interactive version of the infographics, click on the images above or on the following link, which leads to a page of [Tableau](https://www.tableau.com/) Public: <br>

- [Just Repeat-Hit (interactive version)](https://public.tableau.com/views/ProgettodiDataVisualization-I/DataVisualization?:display_count=y&:toolbar=n&:origin=viz_share_link)


<a name="references"></a>
## &#9741; &nbsp; References

[1] Guy Harrison (2015), *Next Generation Databa-ses: NoSQL and Big Data*, Apress, Berkely (CA), USA, 1st ed

<a name="data"></a>
## &#9741; &nbsp; Data
The data necessary for the development of what is described in the Overview has been obtained through the implementation of some scripts in Python language; these were mainly used to make specific requests through the <a href="https://developer.spotify.com/documentation/web-api/">Spotify</a> and <a href="https://docs.genius.com/">Genius</a> APIs, which allowed to obtain, respectively, a list of artists with all the characteristics of the lyrics of the songs for each artist (*lyrics*) with adjoining audiometric peculiarities or, more simply, information relating to the artist or relating to each song.

<a name="presentation"></a>
## &#9741; &nbsp; Presentation
Our slides presentation is available in the <a href="https://github.com/malborroni/Just-Repeat-Hit/blob/master/Slides/Data%20Management/Just%20Repeat-Hit_slides.pdf">Slides</a> folder.<br>
Here we show only the cover:

<p align="center">
  <a href="https://github.com/malborroni/Just-Repeat-Hit/blob/master/Images/intro_official.PNG"><img src = "https://github.com/malborroni/Just-Repeat-Hit/blob/master/Images/intro_official.PNG" width = "90%"></a>
</p>


<a name="aboutus"></a>
## &#9741; &nbsp; About us

&#8860; &nbsp; **Alessandro Borroni** 

- *Current Studies*: Data Science M.Sc. Student at Università degli Studi di Milano-Bicocca (UniMiB);
- *Background*: Bachelor degree in Business Economics at Università degli Studi di Milano-Bicocca (UniMiB).
<br>

<p align = "center">
  <a href = "https://www.linkedin.com/in/alessandro-borroni-212947186/"><img src="https://github.com/malborroni/Foundations_of_Computer-Science/blob/master/images/Linkedin%20logo.png" width = "2.3%"></a>
  <a href = "https://github.com/malborroni/"><img src="https://raw.githubusercontent.com/malborroni/Foundations_of_Computer-Science/master/images/GitHub.png" width = "2.5%"></a>
</p>

&#8860; &nbsp; **Mirko Giugliano**

- *Current Studies*: Data Science M.Sc. Student at Università degli Studi di Milano-Bicocca (UniMiB);
- *Background*: Bachelor degree in Marketing, Business Communication and Global Markets at Università degli Studi di Milano-Bicocca (UniMiB).
<br>

<p align = "center">
  <a href = "https://www.linkedin.com/in/mirko-giugliano/"><img src="https://github.com/malborroni/Foundations_of_Computer-Science/blob/master/images/Linkedin%20logo.png" width = "2.3%"></a>
  <a href = "https://github.com/MirkoGiugliano"><img src="https://raw.githubusercontent.com/malborroni/Foundations_of_Computer-Science/master/images/GitHub.png" width = "2.5%"></a>
</p>

&#8860; &nbsp; **Angela Prade**

- *Current Studies*: Data Science M.Sc. Student at Università degli Studi di Milano-Bicocca (UniMiB);
- *Background*: Bachelor degree in Information Technology at Università di Trento.
<br>

<p align = "center">
  <a href = "https://www.linkedin.com/in/angela-prade-b805b6182/"><img src="https://github.com/malborroni/Foundations_of_Computer-Science/blob/master/images/Linkedin%20logo.png" width = "2.3%"></a>
  <a href = "https://fakelink.com"><img src="https://raw.githubusercontent.com/malborroni/Foundations_of_Computer-Science/master/images/GitHub.png" width = "2.5%"></a>
</p>


