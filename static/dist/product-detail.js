"use strict";
const helperModel = (element, className) => {
    element.classList.toggle(className);
};
const getBackFormHandler = () => {
    const li = document.querySelector('.list--options li');
    const form = document.querySelector('.question');
    const buttonClose = document.querySelector('.close--btn--form');
    const overlay = document.querySelector('.overlay');
    li === null || li === void 0 ? void 0 : li.addEventListener('click', () => {
        helperModel(form, 'back-question');
        helperModel(overlay, 'block--overlay');
    });
    buttonClose.addEventListener('click', () => {
        helperModel(form, 'back-question');
        helperModel(overlay, 'block--overlay');
    });
    overlay.addEventListener('click', () => {
        helperModel(form, 'back-question');
        overlay.classList.remove('block--overlay');
    });
};
getBackFormHandler();
