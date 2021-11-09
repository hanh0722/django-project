"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const axios_1 = __importDefault(require("axios"));
const getCountryWithAPI = () => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const response = yield axios_1.default.get('https://countriesnow.space/api/v0.1/countries/flag/unicode');
        if (response.status >= 400) {
            const error = new Error('cannot get data of countries');
            error.statusCode = 500;
            throw error;
        }
        const data = response.data.data;
        const container = document.querySelector('.list-country');
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
    }
    catch (err) {
        console.log(err);
    }
});
getCountryWithAPI();
