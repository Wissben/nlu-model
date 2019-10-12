import sqlalchemy
import pandas as pd
from geopy.geocoders import Nominatim


def sort_df(df):
    for index, row in df.iterrows():
        score = 4*row['B_ind'] + 2.5*row['B_dom'] + 1.75*row['Exc'] + 1.5*row['N_visites']
        df.iloc[index]['score'] = score

    df = df.sort_values(by='score', ascending=False)
    return df


def get_lat_long(address):
    geolocator = Nominatim(user_agent="newKey")
    location = geolocator.geocode(address)
    if location is not None :
        return location.latitude, location.longitude
    else :
        return location


def clean_df(df):
    nom_espai = list(df['Nom_Espai'])
    nom_distri = list(df['Nom_Distri'])
    nom_barri = list(df['Nom_Barri'])
    coordinates = []
    for i in range (0, len(nom_espai)):
        address = nom_espai[i] + " " + nom_distri[i] + " " + nom_barri[i]
        lat_long = get_lat_long(address)
        #print(df.loc[df.Nom_Espai== nom_espai[i]])
        print(lat_long)
        if lat_long is not None:
            coordinates.append(lat_long)
            df.iloc[i]['latitude'], df.iloc[i]['longitude'] = lat_long
    return df


def clean_df_bis(df):
    nom_espai = list(df['ID_Espai'])
    nom_distri = list(df['Nom_Espai'])
    nom_bari = list(df['C_Distri'])
    coordinates = []
    for i in range (0, len(nom_espai)):
        address = nom_espai[i] + " " + nom_distri[i] + " " + nom_bari[i]
        lat_long = get_lat_long(address)
        print(lat_long)
        if lat_long is not None:
            coordinates.append(lat_long)
            df['latitude'], df['longitude'] = lat_long
    return df


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta


dataset_url = "db.csv"
#df = pd.read_csv(dataset_url, sep='\t|,', engine='python')

df = pd.read_csv(
 dataset_url,
 usecols=lambda col: col not in ["ID_Espani"]
)
print(clean_df(df))

print(df)

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#    print(df)

con, meta = connect('sof', 'password', 'poluted_areas')
print(con)

df.to_sql(name='poluted', con=con, if_exists= 'replace', index=False)

data = pd.read_sql('SELECT * FROM poluted', con)



