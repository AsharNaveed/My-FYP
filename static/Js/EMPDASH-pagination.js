$('#pagination-demo').twbsPagination({
    totalPages: 3,
    startPage: 1,
    visiblePages: 3,
    initiateStartPageClick: true,
    hideOnlyOnePage: false,
    href: false,
    pageVariable: '{{page}}',
    totalPagesVariable: '{{total_pages}}',
    page: null,
    first: 'First',
    prev: 'Previous',
    next: 'Next',
    last: 'Last',
    loop: false,
    beforePageClick: null,
    onPageClick: function (event, page) {
        $('.page-active').removeClass('page-active');
        $('#page'+page).addClass('page-active');
    },
    paginationClass: 'pagination',
    nextClass: 'page-item next',
    prevClass: 'page-item prev',
    lastClass: 'page-item last',
    firstClass: 'page-item first',
    pageClass: 'page-item',
    activeClass: 'active',
    disabledClass: 'disabled',
    anchorClass: 'page-link'
});