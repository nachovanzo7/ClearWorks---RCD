// src/App.jsx
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import Drawer from "./components/Drawer";
import Body from "./components/body";

import Clientes from "./pages/Clientes";
import Coordinaciones from "./pages/Coordinaciones";

import "./styles/App.css";

const App = () => {
  const [headerOpacity, setHeaderOpacity] = useState(1);

  useEffect(() => {
    const handleScroll = () => {
      const scrollTop = window.scrollY;
      let opacidadNueva = 1 - scrollTop / 200;
      if (opacidadNueva < 0.5) opacidadNueva = 0.5;

      setHeaderOpacity(opacidadNueva);
      document.documentElement.style.setProperty(
        "--header-fade-opacity",
        opacidadNueva
      );
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <Router>
      <div className="app-container">
        <Header opacity={headerOpacity} />
        <div className="main-content">
          <Drawer />
          <Body>
            <Routes>
              <Route path="/" element={<Clientes />} />
              <Route path="/coordinaciones" element={<Coordinaciones />} />
            </Routes>
          </Body>
        </div>
      </div>
    </Router>
  );
};

export default App;
