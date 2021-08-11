import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import base64
import seaborn as sns

sns.set()

# heading of the app
st.write("""
# Sales Route Planner
""")

# creating the Input sidebar
st.sidebar.header("Dataframe Uploader")
st.sidebar.markdown("""
[Example format of CSV file](https://github.com/AchuAshwath/Omniway-Technologies-Private-Limited/blob/main/Data%20Test%20-%20Sheet1.csv)
""")

upload_file = st.sidebar.file_uploader("Upload your dataframe as csv file here", type=["csv"])
st.sidebar.write("""***""")

# reading the given csv file
if upload_file is not None:
    data = pd.read_csv(upload_file)
    df = pd.DataFrame(data)
else:
    data = pd.read_csv("Data Test - Sheet1.csv")
    df = pd.DataFrame(data)
    # removing the noisy data
    df = df[df.Latitude < 40]
    # resetting the index numbers
    df = df.reset_index(drop=True)

# showing the input dataframe
st.subheader("User Input Dataframe")
if upload_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example Dataframe  ')
    st.write(df)

st.write("""***""")

# select boxes to select a company name
st.header("Select a Company")
pin_codes = set(df['Pin Code'])
pin_code = st.selectbox('Pin Code', pin_codes)
names_index = []
counter = 0
for i in df['Pin Code']:
    if i == pin_code:
        names_index.append(counter)
    counter = counter + 1

company_names = list(df['Company Name'])
company_names = set(company_names[i] for i in names_index)
company_name = str(st.selectbox('Company Name',company_names))

target = df.index[df['Company Name'] == company_name].tolist()

# creating a model dataframe for clustering
model = df.loc[:, ['Pin Code', 'Latitude', 'Longitude']]

# clustering using the NearestNeighbors
neigh = NearestNeighbors(n_neighbors=11, algorithm='auto').fit(df.loc[:, ['Latitude', 'Longitude']])
neigh_graph = neigh.kneighbors_graph()

# converting the sparse matrix to a dataframe
neigh_graph = pd.DataFrame(neigh_graph.toarray())

# getting indices of true values
pair_values = list(neigh_graph.iloc[target[0]])
indices = []
for i in range(len(pair_values)):

    if pair_values[i] == 1:
        indices.append(i)

# creating a output dataframe
output_df1 = df.iloc[[target[0]]]
output_df2 = df.iloc[indices, :]
output_df = pd.concat([output_df1,output_df2],ignore_index=True)

st.write("""***""")

# displaying Company names and their address
st.write("""# Nearest Companies""")
for j in range(0,12):
    st.write("""##""",j+1,output_df.iloc[j, 0])
    st.write(output_df.iloc[j,1])
st.write("""***""")

# displaying the output dataframe
st.header("Output Dataframe")
st.write(output_df)

# writing the output dataframe
output_df.to_csv(r'output_csv.csv',index=False)

# Hyperlink to download output csv
st.markdown("""
[Output csv file](https://github.com/AchuAshwath/Omniway-Technologies-Private-Limited/blob/main/output_csv.csv)
""")

st.subheader("Use the output csv in [Keplergl](https://kepler.gl/demo) to visualise")
