"use strict";
const helperToggleClassName = (element, className) => {
    element.classList.toggle(className);
};
const getBackOfNavigation = () => {
    const button = document.querySelector('.hamburger');
    const overlay = document.querySelector('.overlay');
    const navigation = document.querySelector('.middle--nav');
    const backButton = document.querySelector('.close--btn');
    const openNavigationHandler = () => {
        helperToggleClassName(overlay, 'block--overlay');
        helperToggleClassName(navigation, 'middle--nav--back');
    };
    backButton.addEventListener('click', openNavigationHandler);
    overlay.addEventListener('click', openNavigationHandler);
    button.addEventListener('click', openNavigationHandler);
};
getBackOfNavigation();
const getSearchingHandler = () => {
    const searchForm = document.querySelector('.search--box');
    const searchButton = document.querySelector('.search--button');
    const model = document.querySelector('.second-model');
    const getFormSearchHandler = () => {
        helperToggleClassName(searchForm, 'search--box--back');
        helperToggleClassName(model, 'block--overlay');
    };
    searchButton.addEventListener('click', getFormSearchHandler);
    model.addEventListener('click', getFormSearchHandler);
};
getSearchingHandler();
const SearchBarInput = () => {
    const input = document.querySelector('.search--input');
    let isTouched = false;
    input.addEventListener('blur', () => {
        isTouched = true;
    });
    input.addEventListener('input', (event) => {
        let isValid = true;
        const value = event.target.value;
        if (isTouched && value.trim().length <= 0) {
            isValid = false;
        }
        // const form = document.querySelector('.search--box')!;
        // if(!isValid){
        //     const p = document.createElement('p');
        //     p.textContent = 'Search is empty!';
        //     p.className = 'error-text'
        //     form.appendChild(p);
        // } else {
        //     const p = form.querySelector('p');
        //     if(!p){
        //         return;
        //     }
        //     form.removeChild(p);
        // }
    });
};
SearchBarInput();
const getAnimatedListFooter = () => {
    const listFooter = document.querySelectorAll('.footer-container ul');
    listFooter.forEach(item => {
        const list = item.querySelectorAll('li');
        list.forEach((element, index) => {
            element.setAttribute('data-aos', 'fade-up');
            element.setAttribute('data-aos-delay', (350 * index).toString());
        });
    });
};
getAnimatedListFooter();
