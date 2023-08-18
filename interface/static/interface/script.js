let quoteScession = document.querySelector("#quote-scession");
let quotes = [`“It’s not a bug. It’s an undocumented feature!”`, `“We don't just build websites, we build websites that SELLS”`, `“Website without visitors is like a ship lost in the horizon.”`]
let index = 0;
let scessions = () => {
    quoteScession.textContent = quotes[index];
    index = (index + 1) % quotes.length;
    setTimeout(scessions, 4000);
}
scessions();

const experience = document.getElementById("experience");
const education = document.getElementById("education");
const skills = document.getElementById("skills");

const exp = document.getElementById("exp");
const edu = document.getElementById("edu");
const skill = document.getElementById("skill");


experience.addEventListener('click', (e) => {
    e.preventDefault()
    exp.style.display = "block";
    edu.style.display = "none";
    skill.style.display = "none";

    experience.style.color = "white";
    education.style.color = "#a0a0a0";
    skills.style.color = "#a0a0a0";
})
education.addEventListener('click', (e) => {
    e.preventDefault()
    exp.style.display = "none";
    edu.style.display = "block";
    skill.style.display = "none";

    experience.style.color = "#a0a0a0";
    education.style.color = "white";
    skills.style.color = "#a0a0a0";
})
skills.addEventListener('click', (e) => {
    e.preventDefault()
    exp.style.display = "none";
    edu.style.display = "none";
    skill.style.display = "block";

    experience.style.color = "#a0a0a0";
    education.style.color = "#a0a0a0";
    skills.style.color = "white";
})
