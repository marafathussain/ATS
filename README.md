#### Application Tracking System (ATS) using the Gemini-Pro
I built it by following an excellent video tutorial by Krish Naik (https://www.youtube.com/watch?v=VZOnp2YpY8Q&t=930s). All credit goes to him.

##### How to run it
First create a new conda environment. For example, here:

```conda create -p ats python==3.10 -y```

Then activate conda enviroment:

```conda activate \path\to\ats\activate```

Then install dependencies:

```pip install -r requirments.txt```

To run the ATS, run the following in the terminal:

```streamlit run app.py```