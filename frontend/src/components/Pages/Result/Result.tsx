import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";

const Result = (props: any) => {
  const { jobs } = props;

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }}>
        <TableHead>
          <TableRow>
            <TableCell>TITLE</TableCell>
            <TableCell align="right">COMPANY</TableCell>
            <TableCell align="right">LOCATION</TableCell>
            <TableCell align="right">URL</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {jobs?.map((row: any) => (
            <TableRow
              key={row.name}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.title}
              </TableCell>
              <TableCell align="right">{row.company}</TableCell>
              <TableCell align="right">{row.location}</TableCell>
              <TableCell align="right">{row.url}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default Result;
