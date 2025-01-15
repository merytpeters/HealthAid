import { useEffect, useState } from "react";
import "../Styles/inventory.css";
import check from "../assets/check.png";
import del from "../assets/delete_icon.png";

import { getRequest } from "../services/apis";

export const Inventory = () => {
  const [res, setRes] = useState({ error: false, data: "" });

  // get already saved inventory
  useEffect(() => {
    const getInventory = async () => {
      const res = await getRequest("inventory");
      setRes(res);
    };

    getInventory();
  });
  const [rows, setRow] = useState([
    {
      drug_name: "",
      quantity: "",
      unit: "",
      expiry_date: "",
      inventory_date: "",
      restock_date: "",
    },
  ]);

  const newStock = () => {
    setRow([
      ...rows,
      {
        drug_name: "",
        quantity: "",
        unit: "",
        expiry_date: "",
        inventory_date: "",
        restock_date: "",
      },
    ]);
  };
  const updateRow = (index, key, value) => {
    const newRows = [...rows];
    newRows[index][key] = value;
    setRow(newRows);
  };
  const saveInventory = (index) => {
    console.log("i am saving");
    const newRows = [...rows];
    const data = newRows[index];
    console.log(data);
  };
  const deleteInventory = (index) => {
    console.log("deleting");
    const newRows = rows.filter((_, i) => i !== index);
    setRow(newRows);
  };

  return (
    <div>
      <div className="inventory">
        <table>
          <thead>
            <tr>
              <th>Drug Name</th>
              <th>Quantity</th>
              <th>Unit</th>
              <th>Expiry Date</th>
              <th>Inventory Date</th>
              <th>Restock Date</th>
              {/* <th></th> */}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, index) => (
              <tr key={index}>
                <td>
                  <input
                    type="text"
                    value={row.drug_name}
                    onChange={(e) =>
                      updateRow(index, "drug_name", e.target.value)
                    }
                  />
                </td>
                <td>
                  <input
                    type="number"
                    value={row.quantity}
                    onChange={(e) =>
                      updateRow(index, "quantity", e.target.value)
                    }
                  />
                </td>
                <td>
                  <input
                    type="text"
                    value={row.unit}
                    onChange={(e) => updateRow(index, "unit", e.target.value)}
                  />
                </td>
                <td>
                  <input
                    type="date"
                    value={row.expiry_date}
                    onChange={(e) =>
                      updateRow(index, "expiry_date", e.target.value)
                    }
                  />
                </td>
                <td>
                  <input
                    type="date"
                    value={row.inventory_date}
                    onChange={(e) =>
                      updateRow(index, "inventory_date", e.target.value)
                    }
                  />
                </td>
                <td>
                  <input
                    type="date"
                    value={row.restock_date}
                    onChange={(e) =>
                      updateRow(index, "restock_date", e.target.value)
                    }
                  />
                </td>
                <td className="actions">
                  <img src={check} onClick={() => saveInventory(index)} />
                  <img src={del} onClick={() => deleteInventory(index)} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="new-stock" onClick={newStock}>
          {" "}
          New Stock
        </button>
      </div>
    </div>
  );
};
