from selenium.webdriver.common.by import By


class ItemLocators:

    # TEXT
    TOTAL = (By.XPATH, '//p[@class="b-top__total line"]/span[2]')
    ITEM_PRICE = (By.XPATH, '//div[@class="product-page__aside"]//ins')
    OLD_PRICE_IN_CART = (By.XPATH, '//div[@class="list-item__price-old"]')
    EMPTY_CART = (By.XPATH, '//div[@class="basket-empty__wrap"]/h1')
    REVIEWS = (By.XPATH, '//li[1]/button[@class="product-feedbacks__title"]')

    # BUTTONS
    ADD_TO_CART = (By.XPATH, '//div[@class="product-page__aside"]//div[3]/div/button[2]')
    GO_TO_CART = (By.XPATH, '//div[@class="product-page__aside"]//div[3]/div/a')
    DEL_ITEM_FROM_CART = (By.XPATH, '//button[@class="btn__del j-basket-item-del"]')
    FIRST_SALE_BUTTON = (By.XPATH, '//div[@class="swiper-container "]/ul[1]/li[1]')
    ITEM_ID = (By.XPATH, '//div[@class="product-card-list"]/article[2]/div/a')
    ITEM_SECOND_ID = (By.XPATH, '//div[@class="product-card-list"]/article[3]/div/a')
    ITEM_IMAGE = (By.XPATH, '//canvas[@class="photo-zoom__preview j-image-canvas"]')
    NEXT_IMAGE = (By.XPATH, '//div[@class="thumbs-gallery__big-img j-big-img"]//button[2]')
    CLOSE_IMAGE = (By.XPATH, '//a[@class="j-close popup__close close"]')
    SELLER = (By.XPATH, '//div[@class="product-page__aside"]//a[@class="seller-info__name seller-info__name--link"]')
    ANOTHER_SELLERS = (By.XPATH, '//a[@class="btn-minor j-move-to-sellers"]')
    ADD_TO_CART_FROM_SELLERS = (By.XPATH, '//button[@class="btn-main other-offers__btn j-add-to-basket"]')
    IMAGE_REVIEW = (By.XPATH, '//div[@class="swiper-slide img-plug swiper-slide-active"]/img')
    ALL_REVIEWS = (By.XPATH, '//a[@class="btn-base comments__btn-all"]')
