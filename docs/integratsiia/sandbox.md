# Тестування інтеграції (Sandbox)

<span class="badge badge--done">Тестове середовище еАкциз</span>

Оцініть роботу інтеграції з тестовим середовищем еАкциз без впливу на бойові дані. Усі операції виконуються з тестовим сервером.

<div class="dl dl--page">
<a class="dl__btn dl__btn--gold" href="https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&amp;masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ"><span class="dl__ico">⬇</span><span><b>Конфігурація інтеграції</b><small>v1.0.1.7 від 01.10.2026 · звичайні форми</small></span></a>
<a class="dl__btn" href="https://aedoc.com.ua/download/%d1%80%d0%be%d0%b7%d1%88%d0%b8%d1%80%d0%b5%d0%bd%d0%bd%d1%8f-%d0%b0%d0%b5%d0%b4%d0%be%d0%ba-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d0%b0%d1%86%d1%96%d1%97-bas-%d0%bc%d0%b0%d0%bb%d0%b8/?wpdmdl=961&amp;masterkey=OcfrThd5vLXuNNHUTBwEwV78gnSI2OGMMOViLd_7AeNiCmjAjv9N9ojm0AmCJY_pDjQA0hE6DZtF46YpioVLUur6G0LQWgZCSQjkqyYMdOmA"><span class="dl__ico">⬇</span><span><b>Розширення «Малий бізнес»</b><small>v1.0.1.7 від 01.10.2026 · керовані форми</small></span></a>
<a class="dl__btn" href="https://aedoc.com.ua/download/%d0%bc%d0%be%d0%b4%d1%83%d0%bb%d1%8c-%d0%bf%d1%96%d0%b4%d0%bf%d0%b8%d1%81%d1%83-%d0%b5%d0%b0%d0%ba%d1%86%d0%b8%d0%b7/"><span class="dl__ico">🔐</span><span><b>Служба підпису AEDocSignService</b><small>обов'язкова для обох поставок</small></span></a>
</div>

!!! warning "Передачу даних на продакшн-середовище `api.xtrace.gov.ua` відключено"
    Усі тести виконуються виключно на **sandbox** — жоден документ не потрапляє до реального кабінету еАкциз.

## Сумісність з конфігураціями BAS

AEDOC інтегрується з наступними конфігураціями BAS. Конфігурації, позначені як готові, доступні для завантаження одразу; решта — у розробці або у плані.

| Конфігурація | Тип форм | Статус / завантаження |
|---|---|---|
| **BAS Малий бізнес 2.0** | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Розширення в пакеті](https://aedoc.com.ua/download/%d1%80%d0%be%d0%b7%d1%88%d0%b8%d1%80%d0%b5%d0%bd%d0%bd%d1%8f-%d0%b0%d0%b5%d0%b4%d0%be%d0%ba-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d0%b0%d1%86%d1%96%d1%97-bas-%d0%bc%d0%b0%d0%bb%d0%b8/?wpdmdl=961&masterkey=OcfrThd5vLXuNNHUTBwEwV78gnSI2OGMMOViLd_7AeNiCmjAjv9N9ojm0AmCJY_pDjQA0hE6DZtF46YpioVLUur6G0LQWgZCSQjkqyYMdOmA) |
| **BAS: Управління торговим підприємством для України 1.2 (УТП)** | <span class="form-pill form-pill--ordinary">Звичайні форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS Управління торгівлею, ред. 2.X (УТ) | <span class="form-pill form-pill--ordinary">Звичайні форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| Роздріб для України, ред. 1.0 | <span class="form-pill form-pill--ordinary">Звичайні форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| Бухгалтерія для України, ред. 2.0 | <span class="form-pill form-pill--ordinary">Звичайні форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS Управління торгівлею, ред. 3.5 | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS Управління торгівлею, ред. 3.2 | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS Бухгалтерія ред. 2.0 / Базова / КОРП | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS ERP 2.1 | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS ERP 2.5 та КУП 2.5 | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS Комплексне управління підприємством (КУП) 2.1 | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |
| BAS Роздрібна торгівля 2.2 | <span class="form-pill form-pill--managed">Керовані форми</span> | [⬇ Скачати конфігурацію](https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ) |

!!! warning "Важливо"
    Для решти конфігурацій BAS інтеграція виконується індивідуально. [Зв'яжіться з нами](https://t.me/AEDocBot) — оцінимо трудомісткість та підготуємо адаптоване рішення.

## Порядок дій для початку роботи

Щоб розпочати тестування інтеграції — виконайте кроки нижче. Кожен крок займає 5–15 хвилин.

<div class="wf">

<div class="wf__step">
<strong>Реєстрація в еАкциз</strong>
<span>Зареєструйтесь у тестовому середовищі системи <a href="https://my-sb.xtrace.org.ua/">https://my-sb.xtrace.org.ua/</a></span>
<a class="wf__link" href="../../pershyi-zapusk/reiestratsiia-eo/">Перейти до реєстрації →</a>
</div>

<div class="wf__step">
<strong>Отримати API-токен</strong>
<span>У кабінеті еАкциз згенеруйте токен для доступу до API.</span>
<a class="wf__link" href="../../pershyi-zapusk/api-token/">Як отримати токен →</a>
</div>

<div class="wf__step">
<strong>Інтегруйте тестову конфігурацію</strong>
<span>Зверніться до фахівця, який обслуговує вашу облікову систему, для інтеграції потрібної конфігурації AEDOC — надайте йому цю сторінку.</span>
</div>

<div class="wf__step">
<strong>Налаштувати Майстра нового ЕО</strong>
<span>Введіть API-токен та створіть тестовий економічний оператор.</span>
<a class="wf__link" href="../../pershyi-zapusk/pomichnyk-eo/">Інструкція до майстра →</a>
</div>

<div class="wf__step">
<strong>Отримати тестові АЕД</strong>
<span>Якщо потрібно надіслати або отримати тестовий АЕД — зверніться у службу підтримки. Ми зробимо тестові документи з даними для вашої системи.</span>
<a class="wf__link" href="https://t.me/AEDocBot">Зв'язатись з підтримкою →</a>
</div>

</div>

## Оберіть спосіб тестування

<div class="ways">

<div class="way">
<div class="way__icon way__icon--desktop">💻</div>
<h3>Спосіб 1. Встановити на свій ПК</h3>
<p class="way__sub">Повноцінне тестування з власною тестовою базою</p>
<ol>
<li><strong>Інтегрувати конфігурацію</strong> — розширення «Малий бізнес» або готову тестову базу УТП 1.2 (див. <a href="#сумісність-з-конфігураціями-bas">таблицю сумісності</a> вище).</li>
<li><strong>Встановити службу підпису</strong> AEDocSignService для роботи з ключем КЕП.</li>
</ol>
<p><a class="way__btn way__btn--outline" href="../../pershyi-zapusk/pomichnyk-eo/">📖 Інструкція до майстра ЕО</a></p>
<div class="creds">
<div><span>API-адреса:</span> <b>sandbox</b></div>
<div><span>Токен API:</span> <b><a href="../../pershyi-zapusk/api-token/">отримується у кабінеті еАкциз</a></b></div>
</div>
</div>

<div class="way">
<div class="way__icon way__icon--web">🌐</div>
<h3>Спосіб 2. Спробувати в браузері</h3>
<p class="way__sub">Швидкий огляд у демо-конфігурації «Малий бізнес»</p>
<p>Без встановлення. Відкрийте демо-базу в браузері та подивіться як виглядає робота з АЕД у конфігурації «Малий бізнес» (керовані форми). Демо підключено до тестового сервера еАкциз.</p>
<p><strong>Що можна перевірити:</strong></p>
<ul>
<li>Список економічних операторів</li>
<li>Створення і підпис АЕД</li>
<li>Робочий стіл АЕД з фільтрами</li>
<li>Сканування акцизних марок</li>
</ul>
<p><a class="way__btn way__btn--gold" href="https://demo.aedoc.com.ua:8080/unftest/en_US/">🚀 Відкрити демо в браузері</a></p>
<div class="creds">
<div><span>URL:</span> <b>https://demo.aedoc.com.ua:8080/unftest/en_US/</b></div>
<div><span>Логін:</span> <b>Адміністратор</b></div>
<div><span>Пароль:</span> <b>demo</b></div>
</div>
<p class="way__note">💡 Демо-база спільна для всіх користувачів. Не вводьте реальних даних. Всі створені документи автоматично видаляються раз на добу.</p>
</div>

</div>

<div class="cta">
<p class="cta__title">Потрібні тестові АЕД для перевірки?</p>
<p>Наша команда може підготувати тестові акцизні документи з потрібними для вас даними — щоб ви могли перевірити реальні сценарії роботи (прийняття, підпис, відхилення, ПпН) у вашій системі.</p>
<a class="way__btn way__btn--gold" href="https://t.me/AEDocBot">Зв'язатись з підтримкою</a>
</div>
