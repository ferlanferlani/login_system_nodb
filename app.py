import streamlit as st
from streamlit_option_menu import option_menu

menu_selected = option_menu(
 menu_title="Welocome to streamlit login system",
 options=['home', 'signup', 'login'],
 orientation="horizontal",
 icons=['house', 'door', 'signup']
)

# menu tab login
if menu_selected == "home":
 st.header("this is home menu")
 
elif menu_selected == "login":
 username_login = st.text_input(
  "silahkan masukkan username"
  )
 password_login = st.text_input(
  "silahkan masukkan password",
  type="password"
  )
 
 login = st.button("login")
 # end menu tab login
 
   # logic login
 if login:
  if username_login == username_signup and password_login == password_signup:
   st.success("anda berhasil login")
  else:
   st.error("anda gagal login")
   # end logic login
 
 # menu tab signup
elif menu_selected == "signup":
 username_signup = st.text_input(
  "silahkan input username"
  )
 password_signup = st.text_input(
  "silahkan masukkan password",
  type="password"
  )
 
 button_signup = st.button("submit")
 # end menu tab signup
 
 # logic add user for save data from input signup
 if button_signup:
  st.success("berhasil menambahkan user")
 else:
  st.error("gagal menambahkan user")
 
  



