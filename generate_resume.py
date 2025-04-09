from jinja2 import Template
import os
import shutil
from datetime import datetime
from bs4 import BeautifulSoup
import configparser
import json

# 新增配置初始化
config = configparser.ConfigParser()
config.read('resume_config.ini', encoding='utf-8')

# 路径配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESUME_TEMPLATE = os.path.join(BASE_DIR, 'resume/resume.html')
OUTPUT_DIR = os.path.join(BASE_DIR, 'myresume')
PATH_PREFIX = '../'  # 路径前缀配置项

# 资源文件映射
RESOURCE_PATHS = {}

def setup_resume_env():
    # 创建目标目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 检查模板文件是否存在
    if not os.path.exists(RESUME_TEMPLATE):
        print(f"错误：模板文件不存在: {RESUME_TEMPLATE}")
        return
    
    # 复制模板文件
    timestamp = datetime.now().strftime('%Y%m%d-%H%M')
    with open(RESUME_TEMPLATE, encoding='utf-8') as f:
        template_content = f.read()
    
    # 准备中英文配置数据
    config_dict = prepare_multilingual_config()
    
    # 添加资源文件夹配置
    resource_folders = config['Preferences']['resource_folders'].split(', ')
    for folder in resource_folders:
        src = os.path.join(BASE_DIR, folder)
        dst = os.path.join(OUTPUT_DIR, folder)
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
    
    # 创建语言切换JS文件
    create_language_switch_js(config_dict)
    
    # 创建Jinja2模板
    template = Template(template_content)
    
    # 渲染模板并写入文件
    rendered = template.render(**config_dict)
    
    # 使用BeautifulSoup进一步处理HTML
    soup = BeautifulSoup(rendered, 'html.parser')
    
    # 添加语言切换按钮
    add_language_switch_button(soup)
    
    # 添加多语言支持
    add_multilingual_support(soup)
    
    # 保存处理后的HTML
    with open(os.path.join(OUTPUT_DIR, f'resume_{timestamp}.html'), 'w', encoding='utf-8') as f:
        f.write(str(soup))
    with open(os.path.join(OUTPUT_DIR, 'myresume.html'), 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"简历已成功生成: {os.path.join(OUTPUT_DIR, 'myresume.html')}")

def prepare_multilingual_config():
    """准备中英文配置数据"""
    config_dict = {'zh': {}, 'en': {}}
    
    for section in config.sections():
        config_dict['zh'][section] = {}
        config_dict['en'][section] = {}
        
        for key, value in config.items(section, raw=True):
            # 处理英文键值对
            if key.endswith('_en'):
                base_key = key[:-3]  # 移除 _en 后缀
                config_dict['en'][section][base_key] = value
            # 处理中文键值对
            elif not key.endswith('_en'):
                config_dict['zh'][section][key] = value
                # 如果没有对应的英文版本，使用中文版本
                en_key = f"{key}_en"
                if en_key not in config[section]:
                    config_dict['en'][section][key] = value
    
    # 添加默认语言设置
    default_lang = config.get('Preferences', 'default_language', fallback='zh')
    config_dict['default_language'] = default_lang
    
    return config_dict

def create_language_switch_js(config_dict):
    """创建语言切换JS文件"""
    js_dir = os.path.join(OUTPUT_DIR, 'js')
    os.makedirs(js_dir, exist_ok=True)
    
    js_content = """
// 语言数据
const languageData = %s;

// 当前语言
let currentLanguage = localStorage.getItem('language') || languageData.default_language;

// 切换语言函数
function switchLanguage() {
    currentLanguage = currentLanguage === 'zh' ? 'en' : 'zh';
    localStorage.setItem('language', currentLanguage);
    applyLanguage();
}

// 应用语言设置
function applyLanguage() {
    const elements = document.querySelectorAll('[data-lang]');
    elements.forEach(element => {
        const key = element.getAttribute('data-lang');
        const [section, field] = key.split('.');
        if (languageData[currentLanguage][section] && languageData[currentLanguage][section][field]) {
            element.textContent = languageData[currentLanguage][section][field];
        }
    });
    
    // 更新语言切换按钮文本
    const switchBtn = document.getElementById('language-switch');
    if (switchBtn) {
        switchBtn.textContent = languageData[currentLanguage]['UI']['language_switch'];
    }
}

// 页面加载完成后应用语言设置
document.addEventListener('DOMContentLoaded', applyLanguage);
""" % json.dumps(config_dict, ensure_ascii=False)
    
    with open(os.path.join(js_dir, 'language-switch.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)

def add_language_switch_button(soup):
    """添加语言切换按钮"""
    # 添加按钮样式
    style = soup.new_tag('style')
    style.string = """
    .language-switch-btn {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        padding: 8px 16px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
    }
    .language-switch-btn:hover {
        background-color: #0056b3;
    }
    """
    
    # 添加样式到页面头部
    if soup.head:
        soup.head.append(style)
    
    # 创建按钮元素
    button = soup.new_tag('button')
    button['id'] = 'language-switch'
    button['onclick'] = 'switchLanguage()'
    button['class'] = 'language-switch-btn'
    button.string = config.get('UI', 'language_switch', fallback='切换语言')
    
    # 尝试多种方式添加按钮
    # 1. 尝试添加到header
    header = soup.select_one('header')
    if header:
        header.insert(0, button)
    # 2. 如果没有header，尝试添加到body开始位置
    elif soup.body:
        soup.body.insert(0, button)
    
    # 添加语言切换脚本
    script = soup.new_tag('script')
    script['src'] = 'js/language-switch.js'
    if soup.body:
        soup.body.append(script)

def add_multilingual_support(soup):
    """为HTML元素添加多语言支持"""
    # 添加标题
    title_elem = soup.select_one('title')
    if title_elem:
        title_elem['data-lang'] = 'PersonalInfo.name'
    
    # 添加个人信息
    name_elem = soup.select_one('h1')
    if name_elem:
        name_elem['data-lang'] = 'PersonalInfo.name'
    
    # 处理所有可能的文本元素
    process_text_elements(soup)
    
    # 添加联系信息
    contact_section = soup.select_one('#contact, .contact')
    if contact_section:
        email_elem = contact_section.select_one('.email')
        if email_elem:
            email_elem['data-lang'] = 'ContactInfo.email'
        
        phone_elem = contact_section.select_one('.phone')
        if phone_elem:
            phone_elem['data-lang'] = 'ContactInfo.phone'
        
        address_elem = contact_section.select_one('.address')
        if address_elem:
            address_elem['data-lang'] = 'ContactInfo.address'
        
        wechat_elem = contact_section.select_one('.wechat')
        if wechat_elem:
            wechat_elem['data-lang'] = 'ContactInfo.wechat'

def process_text_elements(soup):
    """处理所有文本元素，添加data-lang属性"""
    # 教育经历
    education_items = soup.select('#about .data-info')
    if len(education_items) >= 2:
        # 第一个教育经历
        date_elem = education_items[0].select_one('.meta-date')
        if date_elem:
            date_elem['data-lang'] = 'EducationDetails.education_1_date'
        
        title_elem = education_items[0].select_one('.info-title')
        if title_elem:
            title_elem['data-lang'] = 'EducationDetails.education_1_title'
        
        desc_elem = education_items[0].select_one('p')
        if desc_elem:
            desc_elem['data-lang'] = 'EducationDetails.education_1_school'
        
        # 第二个教育经历
        date_elem = education_items[1].select_one('.meta-date')
        if date_elem:
            date_elem['data-lang'] = 'EducationDetails.education_2_date'
        
        title_elem = education_items[1].select_one('.info-title')
        if title_elem:
            title_elem['data-lang'] = 'EducationDetails.education_2_title'
        
        desc_elem = education_items[1].select_one('p')
        if desc_elem:
            desc_elem['data-lang'] = 'EducationDetails.education_2_school'
    
    # 工作经验
    experience_items = soup.select('#about .col-lg-6:nth-of-type(2) .data-info')
    if len(experience_items) >= 2:
        # 第一个工作经验
        date_elem = experience_items[0].select_one('.meta-date')
        if date_elem:
            date_elem['data-lang'] = 'ExperienceDetails.experience_1_date'
        
        title_elem = experience_items[0].select_one('.info-title')
        if title_elem:
            title_elem['data-lang'] = 'ExperienceDetails.experience_1_title'
        
        desc_elem = experience_items[0].select_one('p')
        if desc_elem:
            desc_elem['data-lang'] = 'ExperienceDetails.experience_1_description'
        
        # 第二个工作经验
        date_elem = experience_items[1].select_one('.meta-date')
        if date_elem:
            date_elem['data-lang'] = 'ExperienceDetails.experience_2_date'
        
        title_elem = experience_items[1].select_one('.info-title')
        if title_elem:
            title_elem['data-lang'] = 'ExperienceDetails.experience_2_title'
        
        desc_elem = experience_items[1].select_one('p')
        if desc_elem:
            desc_elem['data-lang'] = 'ExperienceDetails.experience_2_description'
    
    # 处理更多的工作经历项：
    for i in range(1, 7):  # 处理6个工作经历
        experience_selector = f'#experience-{i}' if soup.select_one(f'#experience-{i}') else f'.experience-{i}'
        experience_item = soup.select_one(experience_selector)
        if experience_item:
            date_elem = experience_item.select_one('.date')
            if date_elem:
                date_elem['data-lang'] = f'ExperienceDetails.experience_{i}_date'
            
            title_elem = experience_item.select_one('.title, .position')
            if title_elem:
                title_elem['data-lang'] = f'ExperienceDetails.experience_{i}_title'
            
            desc_elem = experience_item.select_one('.description, p')
            if desc_elem:
                desc_elem['data-lang'] = f'ExperienceDetails.experience_{i}_description'
    
    # 处理技能部分
    skills_section = soup.select_one('#skills, .skills')
    if skills_section:
        for i in range(1, 6):  # 处理5个技能
            skill_item = skills_section.select_one(f'.skill-{i}, .skill:nth-child({i})')
            if skill_item:
                name_elem = skill_item.select_one('.name, .skill-name')
                if name_elem:
                    name_elem['data-lang'] = f'Skills.skill_{i}_name'
                
                percentage_elem = skill_item.select_one('.percentage, .skill-level')
                if percentage_elem:
                    percentage_elem['data-lang'] = f'Skills.skill_{i}_percentage'

def update_resource_paths():
    """更新资源路径"""
    resume_path = os.path.join(OUTPUT_DIR, 'myresume.html')
    
    with open(resume_path, 'r+', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        # 保留原始路径不做修改
        pass
        
        # 写回修改
        f.seek(0)
        f.write(str(soup))
        f.truncate()

if __name__ == '__main__':
    setup_resume_env()
    update_resource_paths()
    print(f'简历环境已成功创建在：{OUTPUT_DIR}')