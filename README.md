# 个人网站项目

## 项目结构

### 主要页面

- **index.html**: 网站主页，包含作品集展示、关于我、经验、作品和联系方式等部分
- **blog.html**: 博客页面，展示文章列表
- **contact.html**: 联系页面，包含联系表单
- **portfolio-masonry.html**: 作品集瀑布流展示页面
- **single-portfolio.html**: 单个作品详情页面
- **single-post.html**: 单篇博客文章页面
- **team.html**: 团队成员展示页面
- **styles.html**: 样式展示页面，包含网站使用的各种UI组件

### 特殊内容页面

- **zone.html**: 中文文章《重生之金融沙皇》
- **interest.html**: 中文文章《重生之我是央行行长》
- **industry_distribution.html**: 行业分布统计页面（使用Bokeh可视化库）

### 资源文件

- **css/**: 样式文件目录
  - vendor.css: 第三方库样式
- **js/**: JavaScript文件目录
  - jquery-1.11.0.min.js: jQuery库
  - plugins.js: 插件集合（包含anime.js等）
  - script.js: 网站主要脚本文件
- **images/**: 图片资源目录
  - 包含logo、作品集图片、团队成员照片等

## 网站导航结构

网站主要导航包含以下链接：
- Home
- About
- Experience
- Works
- Contact

下拉菜单「Pages」包含以下子页面：
- Single Post
- Single Portfolio
- Contact
- My Team
- Blog
- Portfolio Masonry
- Styles

## 技术栈

- HTML5
- CSS3
- JavaScript
- jQuery
- Bootstrap 5
- Swiper（轮播组件）
- Isotope（布局库）
- Anime.js（动画库）
- Bokeh（数据可视化，用于industry_distribution.html）

## 部署信息

该项目使用GitHub Pages部署，通过GitHub Actions自动化部署流程（见.github/workflows/pages.yml）。