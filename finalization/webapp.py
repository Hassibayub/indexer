import streamlit as st 
from finalization.install_with_py import install
import subprocess


def main():
    st.title("Index builder")
    
    if st.button("Run", type='primary', use_container_width=True):
        with st.spinner("Building index"):
            install()
        
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        output = result.stdout
        st.code(output)

        st.write("Index testing complete!")


if __name__ == '__main__':
    main()