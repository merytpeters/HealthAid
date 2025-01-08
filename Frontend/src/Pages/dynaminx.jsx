import { useState } from "react";

const DynamicTables = () => {
  const [tables, setTables] = useState([]);

  // Function to add a new table
  const addTable = () => {
    setTables([...tables, { rows: [] }]);
  };

  // Function to add a row to a specific table
  const addRow = (tableIndex) => {
    const newTables = [...tables];
    newTables[tableIndex].rows.push({ col1: "", col2: "", col3: "" });
    setTables(newTables);
  };

  // Function to handle input changes in the table
  const handleInputChange = (tableIndex, rowIndex, columnName, value) => {
    const newTables = [...tables];
    newTables[tableIndex].rows[rowIndex][columnName] = value;
    setTables(newTables);
  };

  return (
    <div>
      <button onClick={addTable}>Add Table</button>

      {tables.map((table, tableIndex) => (
        <div key={tableIndex}>
          <table border="1">
            <thead>
              <tr>
                <th>Drug Name</th>
                <th>Quantity</th>
                <th>Unit</th>
                <th>Expiry Date</th>
                <th>Inventory Date</th>
                <th>Restock Date</th>
              </tr>
            </thead>
            <tbody>
              {table.rows.map((row, rowIndex) => (
                <tr key={rowIndex}>
                  <td>
                    <input
                      type="text"
                      value={row.col1}
                      onChange={(e) =>
                        handleInputChange(
                          tableIndex,
                          rowIndex,
                          "col1",
                          e.target.value
                        )
                      }
                    />
                  </td>
                  <td>
                    <input
                      type="text"
                      value={row.col2}
                      onChange={(e) =>
                        handleInputChange(
                          tableIndex,
                          rowIndex,
                          "col2",
                          e.target.value
                        )
                      }
                    />
                  </td>
                  <td>
                    <input
                      type="text"
                      value={row.col3}
                      onChange={(e) =>
                        handleInputChange(
                          tableIndex,
                          rowIndex,
                          "col3",
                          e.target.value
                        )
                      }
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <button onClick={() => addRow(tableIndex)}>Add Row</button>
        </div>
      ))}
    </div>
  );
};

export default DynamicTables;
