import axios from 'axios';
import { getRefreshedToken,isAccessTokenExpired,setAuthUser } from './auth';
import { API_BASE_URL } from './constants';
import Cookies from 'js-cookie';

const useAxios = ()=>{
    const accessToken=Cookies.get("access_token");
    const refreshToken=Cookies.get("refresh_token");
    
}
