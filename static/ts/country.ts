import axios, { AxiosResponse } from "axios";

interface Country {
    name: string,
    unicodeFlag: string
}
interface typeCountry extends AxiosResponse {
    data: {
        data: Array<Country>
    }
}
interface error extends Error{
    statusCode?: number
}
const getCountryWithAPI = async () => {
    try{
        const response: typeCountry = await axios.get('https://countriesnow.space/api/v0.1/countries/flag/unicode');
        if(response.status >= 400){
            const error: error = new Error('cannot get data of countries');
            error.statusCode = 500;
            throw error;
        }
        const data = response.data.data;
        const container = document.querySelector('.list-country')!;
        // data.forEach(item => {
        //     const li = document.createElement('li');
        //     const name = document.createElement('span');
        //     name.textContent = item.name;
        //     const flag = document.createElement('span');
        //     flag.textContent = item.unicodeFlag;
        //     li.appendChild(name);
        //     li.appendChild(flag);
        //     container.appendChild(li);
        // })
        
    }catch(err){
        console.log(err);
    }
    
}

getCountryWithAPI();