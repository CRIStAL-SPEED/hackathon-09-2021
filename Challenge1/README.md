# Challenge 1 : Air quality 

## Objectives 

The goal of this challenge is to estimate a pollution pike at day 2 and day 3. 

## Challenge resources

### Station localization 

Raw data available 
Study area:

    POLYGON ((3.01025390625 42.946622264045786, 3.2522964477539062 42.946622264045786, 3.2522964477539062 43.07841776257431, 3.01025390625 43.07841776257431, 3.01025390625 42.946622264045786))

```
Coordinates   Latitude      Longitude
Point 1       42.94662      3.010253        
Point 2       43.078417     3.252296

Lat/long of AIR probes (identification de la zone d’étude) :
Station       Latitude      Longitude        Station name
868           43.01492      3.05215          Piscine
869           43.01404      3.06448          Capitainerie
```

### Dataset 

The following dataset (https://nextcloud.univ-lille.fr/index.php/s/wMrnn2ZcHBtGrAj) contained these fields:
 * Raw data of air quality station: 
 * Fine particle concentration (anonymized data)
  * Weather data: wind, rain
  * Maritime traffic data of the studied area
  * Coordinate data of the study area
  * Coordinate data of AIR quality stations 

### Thresholds for pollution detection 

Alert thresholds for measurements PM10, NO2 et SO2 

 * First threshold (threshold of pre-alert) :
    * PM 10 and PM25 >= 50 μg/mᴲ (on average over 24 hours),
    * NO₂ >= 200 μg/mᴲ (on average over 1 hour )
    * SO₂ >= 300 μg/mᴲ (on average over 1 hour )

 * Second threshold (threshold of alert) :
    * PM 10 and PM 25 >= 80 μg/mᴲ (on the last 24h)
    * NO₂ >= 300 μg/mᴲ (on the last hour)
    * SO₂ >= 500 μg/mᴲ (on the last hour)

## Tools
### Environment
There is an example [SPEED_Hackathon.ipynb](to fill) of data manipulation and simple daily average PM10 predictions written with Jupyter Notebook, and it's recommended that you develop your codes with the same tool.  

If you are using Windows : install [Anaconda](https://www.anaconda.com/products/individual).    
If you are using Linux : `pip3 install Jupyter`  

Then you can create a new virtual environment: (in Windows: launch **Anaconda Prompt**)
```
# Create new virtual environment
conda create -n Hackathon python=3.6   

# Activate virtual env.
conda activate Hackathon  

# Install required packages
pip install -r requirements.txt
```  
### Libraries
The used data processing library is Pandas, you can check its [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) class documentation to explore more methods for time stamped data manipulation. It would be of great help if you have knowledge and experience in using Numpy.  

The used machine learning library is Scikit-Learn. You can check its [Supervised Learning](https://scikit-learn.org/stable/supervised_learning.html) tutorial to find all linear and non-linear **regression** algorithms provided by Scikit-Learn.
