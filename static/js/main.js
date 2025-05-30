function scrolltoLeft(button) {
    console.log(button)
    let wrapper = document.querySelector(`#${button.getAttribute('target')} .wrapper`)
    let w = wrapper.querySelector('.c-item').getBoundingClientRect().width

    let currentScroll = wrapper.scrollLeft

    wrapper.scroll({
        left: currentScroll - w,
        behavior: "smooth",
    });

}


function scrolltoRight(button) {
    console.log(button)
    let wrapper = document.querySelector(`#${button.getAttribute('target')} .wrapper`)
    let w = wrapper.querySelector('.c-item').getBoundingClientRect().width

    let currentScroll = wrapper.scrollLeft

    wrapper.scroll({
        left: currentScroll + w,
        behavior: "smooth",
    });

}