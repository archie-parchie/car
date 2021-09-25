def app(final_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(final_df)

    # Display descriptive statistics.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(final_df.describe())    
    # ADD NEW CODE FROM HERE
    beta_column1,beta_column2,beta_column3=st.beta_columns(3)
    with beta_column1:
      if st.checkbox("Show all column names"):
        st.table(final_df.columns)
    with beta_column2:
      if st.checkbox("View column data type"):
        st.table(final_df.dtypes)
    with beta_column3:
      if st.checkbox("View column data"):
        col=st.selectbox("Select a column",tuple(final_df.columns))
        st.write(final_df[col])