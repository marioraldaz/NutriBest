import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { Filters } from "./Filters";
import { CardsList } from "../Lists/CardsList";

export function Searchbar({ filters, fetchByName, complexFetch }) {
  const { register, handleSubmit } = useForm();
  const [products, setProducts] = useState([]);
  const [filterValues, setFilterValues] = useState({});
  const [advancedFilters, setAdvancedFilters] = useState(false);
  const [searched, setSearched] = useState(false);
  const onSubmit = async (data) => {
    let productsFetched = [];
    advancedFilters
      ? (productsFetched = await complexFetch({ ...filterValues }))
      : (productsFetched = await fetchByName(data.search));
    setProducts(productsFetched);
    console.log(productsFetched);
    setSearched(true);
  };

  const handleFilterChange = (name, value) => {
    setFilterValues((prevValues) => ({
      ...prevValues,
      [name]: value,
    }));
  };

  const changeAdvancedVisibility = (event) => {
    event.preventDefault();
    setAdvancedFilters(!advancedFilters);
  };

  return (
    <form
      className="w-full flex justify-center items-center flex-col mx-auto"
      onSubmit={handleSubmit(onSubmit)}
    >
      <label
        htmlFor="default-search"
        className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
      >
        Search
      </label>
      {!advancedFilters && (
        <div className="relative w-2/3">
          <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
            <svg
              className="w-4 h-4 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
          </div>
          <input
            type="search"
            id="default-search"
            {...register("search", { required: true })}
            className="bg-transparent block w-full p-4 ps-10 text-sm text-white border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Search Mockups, Logos..."
            required
          />
          <button
            type="submit"
            className="text-white absolute end-2.5 bottom-2.5 bg-green-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Search
          </button>
        </div>
      )}
      <button
        onClick={changeAdvancedVisibility}
        className="mt-4 w-44 h-12 bg-neutral-800 rounded-lg"
      >
        {!advancedFilters ? "Show" : "Hide"} Advanced Filters
      </button>

      {advancedFilters && (
        <div className="w-2/3 mb-[80px]">
          <Filters
            filters={filters}
            onFilterChange={handleFilterChange}
            onSubmit={onSubmit}
          />
        </div>
      )}
      {products.length > 0 && (
        <div className="flex items-center justify-center">
          <div className="flex flex-wrap justify-center items-center p-4  ">
            <CardsList products={products} />
          </div>
        </div>
      )}
      {products.length <= 0 && searched && <h1>No Results Found :c</h1>}
    </form>
  );
}
