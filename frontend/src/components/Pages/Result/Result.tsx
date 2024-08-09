import * as React from "react";
import {
  Box,
  Link,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from "@mui/material";
import LaunchIcon from "@mui/icons-material/Launch";

const Result = (props: any) => {
  const { jobs } = props;

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }}>
        <TableHead>
          <TableRow>
            <TableCell align="left">TITLE</TableCell>
            <TableCell align="left">COMPANY</TableCell>
            <TableCell align="left">LOCATION</TableCell>
            {/* <TableCell align="right">URL</TableCell> */}
          </TableRow>
        </TableHead>
        <TableBody>
          {jobs?.map((row: any) => (
            <TableRow
              key={row.name}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row" align="left">
                <Box
                  sx={{
                    display: "flex",
                    alignItems: "center",
                  }}
                >
                  <Typography sx={{ mr: 2 }}>{row.title}</Typography>
                  <a
                    href={row.url}
                    target="_blank"
                    rel="noreferrer"
                    style={{ display: "flex", alignItems: "center" }}
                  >
                    <LaunchIcon fontSize="small" />
                  </a>
                </Box>
              </TableCell>
              <TableCell align="left">{row.company}</TableCell>
              <TableCell align="left">{row.location}</TableCell>
              {/* <TableCell align="right"></TableCell> */}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default Result;
