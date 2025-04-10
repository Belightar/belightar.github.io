import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">首页</Link></li>
          <li><Link to="/interest">兴趣</Link></li>
          <li><Link to="/zone">空间</Link></li>
          <li><Link to="/projects">项目</Link></li>
          <li><Link to="/contact">联系</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/interest" element={<Interest />} />
        <Route path="/zone" element={<Zone />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  );
}

export default App;  // 确保有默认导出