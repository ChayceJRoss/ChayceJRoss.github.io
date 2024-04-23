return {
    {
      Math = function (elem)
        if elem.mathtype == "DisplayMath" then
            elem.text = elem.text:gsub("[\n\r]","")
            return elem
        end
      end,
    }
  }