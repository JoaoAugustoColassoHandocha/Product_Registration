import streamlit as st
import os

# Page title
st.title('Product Registration')

# Sidebar for selecting actions
option = st.sidebar.selectbox('Select an option', ('Add Product', 'List Products'))

# Simulated dictionary of a products database
products = [

    {'ID': 1, 'Name': 'Pineapple', 'Price': 5.99},
    {'ID': 2, 'Name': 'Avocado', 'Price': 4.99},
    {'ID': 3, 'Name': 'Banana', 'Price': 1.99}
  
]

# Function to list products
def list_products():
    
    st.subheader('Product List')
  
    for product in products:
      
        st.write(f'ID: {product['ID']}, Name: {product['Name']}, Price: {product['Price']}')

# Function for Add product
def add_product():
    
    st.subheader('Add product')
    
    name = st.text_input('Product name')
    
    price = st.number_input('Product price')
    
    if st.button('To add'):
        
        new_product = {'ID': len(products) + 1, 'Name': name, 'Price': price}
        
        products.append(new_product)
        
        st.sucess('Product added successfully!')

# Logic for selected options in the sidebar
if option == 'Add product':
    
    add_product()

elif option == 'List products':
    
    list_products()