import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import React, { createContext, useState } from "react";
import { COURSE_URL } from '../config/config'

export const CourseContext = createContext();

export const CourseProvider = ({children}) => {
    const [courseInfo, setCourseInfo] = useState({});

    const get_course = () => {
        axios
            .get(`${COURSE_URL}list/`, {})
            .then(res => {
                let courseInfo = res.data[2];
                setCourseInfo(courseInfo);
                AsyncStorage.setItem('courseInfo', JSON.stringify(courseInfo));
                
            })
            .catch(e => {
                console.log(`course error ${e}`)
            });
    };

    return (
        <CourseContext.Provider 
            value={{
                get_course,
                courseInfo,
            }}
        >{children}</CourseContext.Provider>
    );
    
};