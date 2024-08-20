# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline
from streamlit_option_menu import option_menu
import pages as pgs


st.set_page_config(page_title="法国绘画展-瓦力AI解读", layout="wide")

def main():

    selected2 = option_menu(None, ["法国绘画作品", "绘画故事", "绘画解读", '绘画风格'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    #selected2
    
    if selected2 == "法国绘画作品":
        st.session_state.page = '法国绘画作品'
        # load data
        with open('example1.json', "r") as f:
            data1 = f.read()

        # render timeline
        timeline(data1, height=800)

        # load data
        with open('example2.json', "r") as f:
            data2 = f.read()

        # render timeline
        timeline(data2, height=800)

        # load data
        with open('example3.json', "r") as f:
            data3 = f.read()

        # render timeline
        timeline(data3, height=800)

        # load data
        with open('example4.json', "r") as f:
            data4 = f.read()

        # render timeline
        timeline(data4, height=800)

        # load data
        with open('example5.json', "r") as f:
            data5 = f.read()

        # render timeline
        timeline(data5, height=800)

        # load data
        with open('example6.json', "r") as f:
            data6 = f.read()

        # render timeline
        timeline(data6, height=800)

        # load data
        with open('example7.json', "r") as f:
            data7 = f.read()

        # render timeline
        timeline(data7, height=800)

if __name__ == '__main__':
    main()