# Anita Soroush
import pandas as pd
import matplotlib.pyplot as plot


class CrimesAnalysis:
      def __init__(self, df_2015_address, df_2016_address, df_2017_address, df_2018_address, df_2019_address):
            self.df = pd.concat(map(pd.read_csv, [df_2015_address,
                                                  df_2016_address,
                                                  df_2017_address,
                                                  df_2018_address,
                                                  df_2019_address]), ignore_index=True)
            self.crimes = ["ASSAULT", "THEFT/LARCENY", "DRUGS/ALCOHOL VIOLATIONS", "OTHER", "VEHICLE BREAK-IN/THEFT",
                           "VANDALISM", "BURGLARY", "FRAUD", "MOTOR VEHICLE THEFT", "ROBBERY", "WEAPONS", "SEX CRIMES",
                           "DISTURBING THE PEAS", "HOMICIDE", "ARSON", "DUI"]
            self.mean_o_to_r = []
            print(self.df.head())
            print(self.df.tail())

      def data_cleaner(self):
            self.df = self.df.dropna()

      def crime_counter(self):
             self.df['CRIME_TYPE'].value_counts().plot.bar(color=["#FF0000", "#FF3333", "#FF4A4A",
                                                                  "#FF5E5E", "#FF9292", "#FFAFAF",
                                                                  "#FFC3C3", "#FFCBCB", "#FFD7D7",
                                                                  "#FFD7D7", "#FFD7D7", "#FFD7D7",
                                                                  "#FFD7D7", "#FFD7D7", "#FFD7D7",
                                                                  "#FFD7D7", "#FFD7D7", "#FFD7D7"])
             plot.show()

      def top_10_zip_code(self):
            self.df['ZIP_CODE'].value_counts().nlargest(10).plot.bar(color="#273c75")
            plot.show()

      def trend_of_each_crime(self):
          self.df['YEAR'] = pd.DatetimeIndex(self.df['DATE_REPORTED']).year

          self.crimes = ["ASSAULT", "THEFT/LARCENY", "DRUGS/ALCOHOL VIOLATIONS", "OTHER", "VEHICLE BREAK-IN/THEFT",
                         "VANDALISM", "BURGLARY", "FRAUD", "MOTOR VEHICLE THEFT", "ROBBERY", "WEAPONS", "SEX CRIMES",
                         "DISTURBING THE PEAS", "HOMICIDE", "ARSON", "DUI"]
          for crime in self.crimes:
              self.df[self.df['CRIME_TYPE'] == crime]['YEAR'].value_counts().sort_index().plot(color="#833471", title ="reported "+crime+" in last 5 years")
              plot.show()

      def occurrence_to_report(self):
          self.df["OCCURRENCE_TO_REPORT"] = (pd.to_datetime(self.df['DATE_OCCURED']) -
                                             pd.to_datetime(self.df["DATE_REPORTED"])).values.astype(int)
          for crime in self.crimes:
              self.mean_o_to_r.append(self.df[self.df['CRIME_TYPE'] == crime]["OCCURRENCE_TO_REPORT"].mean())

          data_frame = pd.DataFrame(
              {'crime type': self.crimes,
               'mean time span between occurrence to report': self.mean_o_to_r})
          data_frame.plot(kind="bar", color='#006266')
          plot.show()


if __name__ == "__main__":
    crime_ana = CrimesAnalysis('Crime_Data_2015.csv',
                               'Crime_Data_2016.csv',
                               'Crime_Data_2017.csv',
                               'Crime_Data_2018.csv',
                               'Crime_Data_2019.csv')
    crime_ana.data_cleaner()
    crime_ana.crime_counter()
    crime_ana.top_10_zip_code()
    crime_ana.trend_of_each_crime()
    crime_ana.occurrence_to_report()
