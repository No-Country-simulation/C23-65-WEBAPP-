import { BrowserRouter, Route, Routes } from "react-router";
import { Home } from "./pages/home/home";
import { InternationalGalleryHub } from "./pages/InternationalGalleryHub/InternationalGalleryHub";
import { Gallery } from "./pages/Gallery/Gallery";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index path="/login" element={<Home />} />
          {/* <Route path="/hall" element={<Hall />} /> */}
          <Route
            path="/galeria-internacional"
            element={<InternationalGalleryHub />}
          />
          <Route path="/galeria" element={<Gallery />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
