// Базовый путь до API.
// Так как фронтенд отдается тем же FastAPI-приложением,
// достаточно относительного пути "/".
const API_BASE = "/";

/**
 * Универсальная функция для выполнения GET-запроса к API и парсинга JSON.
 * @param {string} url - путь до эндпоинта
 * @returns {Promise<any>} - данные в формате JSON
 */
async function fetchJson(url) {
    const response = await fetch(url);
    if (!response.ok) {
        // Если сервер вернул ошибку - выкинем исключение,
        // чтобы можно было показать alert
        const text = await response.text();
        throw new Error(`Ошибка загрузки ${url}: ${response.status} ${text}`);
    }
    return await response.json();
}

/**
 * Рендер таблицы: очищает tbody и заполняет строками по массиву rows.
 * @param {HTMLTableSectionElement} tableBody - tbody таблицы
 * @param {Array<object>} rows - список объектов (строки)
 * @param {Array<string>} columns - порядок и набор полей для отображения
 */
function renderTableBody(tableBody, rows, columns) {
    tableBody.innerHTML = "";
    for (const row of rows) {
        const tr = document.createElement("tr");
        for (const col of columns) {
            const td = document.createElement("td");
            td.textContent = row[col];
            tr.appendChild(td);
        }
        tableBody.appendChild(tr);
    }
}

/**
 * Загрузить список статей.
 * Использует фильтры: статус и ID автора.
 */
async function loadArticles() {
    // Берем значения фильтров из DOM
    const status = document.getElementById("articleStatusFilter").value;
    const authorId = document.getElementById("articleAuthorIdFilter").value;

    // Формируем query-параметры
    const params = new URLSearchParams();
    if (status) params.append("status", status);
    if (authorId) params.append("author_id", authorId);

    // Собираем полный URL
    let url = API_BASE + "articles/";
    if ([...params.keys()].length > 0) {
        url += "?" + params.toString();
    }

    try {
        const data = await fetchJson(url);
        const tbody = document.querySelector("#articlesTable tbody");

        // Список колонок совпадает с полями схемы ArticleRead
        renderTableBody(tbody, data, [
            "id",
            "title",
            "status",
            "author_id",
            "category_id",
            "created_at",
        ]);
    } catch (err) {
        alert(err.message);
    }
}

/**
 * Загрузить список комментариев.
 * Фильтр по ID статьи (опционально).
 */
async function loadComments() {
    const articleId = document.getElementById("commentArticleIdFilter").value;

    const params = new URLSearchParams();
    if (articleId) params.append("article_id", articleId);

    let url = API_BASE + "comments/";
    if ([...params.keys()].length > 0) {
        url += "?" + params.toString();
    }

    try {
        const data = await fetchJson(url);
        const tbody = document.querySelector("#commentsTable tbody");

        renderTableBody(tbody, data, [
            "id",
            "article_id",
            "author_name",
            "text",
            "created_at",
        ]);
    } catch (err) {
        alert(err.message);
    }
}

/**
 * Загрузить сводную таблицу "Управление контентом".
 */
async function loadContentSummary() {
    const url = API_BASE + "summary/content-management";
    try {
        const data = await fetchJson(url);
        const tbody = document.querySelector("#contentSummaryTable tbody");

        renderTableBody(tbody, data, [
            "article_title",
            "author_full_name",
            "category_name",
            "status",
        ]);
    } catch (err) {
        alert(err.message);
    }
}

/**
 * Загрузить отчёт "Активность авторов".
 */
async function loadAuthorActivity() {
    const url = API_BASE + "summary/author-activity";
    try {
        const data = await fetchJson(url);
        const tbody = document.querySelector("#authorActivityTable tbody");

        renderTableBody(tbody, data, [
            "author_full_name",
            "published_articles",
            "total_comments",
        ]);
    } catch (err) {
        alert(err.message);
    }
}

/**
 * Инициализация: навешиваем обработчики на кнопки
 * и один раз загружаем данные при открытии страницы.
 */
document.addEventListener("DOMContentLoaded", () => {
    // Кнопки фильтрации/загрузки
    document
        .getElementById("loadArticlesBtn")
        .addEventListener("click", loadArticles);

    document
        .getElementById("loadCommentsBtn")
        .addEventListener("click", loadComments);

    document
        .getElementById("loadContentSummaryBtn")
        .addEventListener("click", loadContentSummary);

    document
        .getElementById("loadAuthorActivityBtn")
        .addEventListener("click", loadAuthorActivity);

    // Авто-загрузка данных при первом открытии
    loadArticles();
    loadComments();
    loadContentSummary();
    loadAuthorActivity();
});
