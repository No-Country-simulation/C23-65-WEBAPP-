import PropTypes from "prop-types";
import { useState } from "react";
import { FaChevronDown, FaChevronUp } from "react-icons/fa";
import { Link } from "react-router";

export const Accordion = ({ section }) => {
  const [activeIndex, setActiveIndex] = useState(null);

  const handleClick = (index) => {
    setActiveIndex(index === activeIndex ? null : index);
  };

  return (
    <div className="accordion w-5/6 mx-auto">
      {section.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header w-full flex flex-row justify-between bg-gray-200 p-4 border-b border-gray-300 hover:bg-gray-300 transition-colors duration-300  text-text-secondary ${
              activeIndex === index ? "font-bold" : ""
            }`}
            onClick={() => handleClick(index)}
          >
            <span>{item.title}</span>
            <span>
              {activeIndex === index ? <FaChevronUp /> : <FaChevronDown />}
            </span>
          </button>
          <div
            className={`accordion-content overflow-hidden transition-all duration-500 ease-in-out px-4 ${
              activeIndex === index ? "max-h-96 py-2" : "max-h-0 p-0"
            }`}
          >
            {item.links.map((link) => (
              <ul key={link.tag}>
                <Link to={link.href}>{link.tag}</Link>
              </ul>
            ))}
          </div>
        </div>
      ))}
      {/* <div className="accordion-item">
        <button
          className="accordion-header w-full text-left bg-gray-200 p-4 border-b border-gray-300 hover:bg-gray-300 transition-colors duration-300"
          onClick={() => handleClick(0)}
        >
          Sección 1
        </button>
        <div
          className={`accordion-content overflow-hidden transition-all duration-200 ease-linear ${
            activeIndex === 0 ? "max-h-96 py-2" : "max-h-0 p-0"
          }`}
        >
          <p>
            Este es el contenido de la sección 1. Puede ser texto o cualquier
            otro contenido.
          </p>
        </div>
      </div> */}
    </div>
  );
};

Accordion.propTypes = {
  section: PropTypes.array.isRequired,
};
