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
};
SearchBarInput();
